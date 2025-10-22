import os
import time
from datetime import date
from typing import Dict, Any, List, Optional

# --- Importaciones de Servicios ---
from python_forestacion.servicios.negocios.fincas_service import FincasService
from python_forestacion.servicios.personal.trabajador_service import TrabajadorService
from python_forestacion.servicios.terrenos.registro_forestal_service import RegistroForestalService 
from python_forestacion.servicios.terrenos.tierra_service import TierraService
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry

# --- Importaciones de Entidades ---
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.entidades.terrenos.plantacion import Plantacion # Importar Plantacion
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna
from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.entidades.personal.apto_medico import AptoMedico
from python_forestacion.entidades.personal.tarea import Tarea
from python_forestacion.entidades.personal.herramienta import Herramienta

# --- Importaciones de Concurrencia (Riego) ---
from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
from python_forestacion.riego.control.control_riego_task import ControlRiegoTask
from python_forestacion.constantes import THREAD_JOIN_TIMEOUT # Importación para detención segura

# --- CRÍTICO: Importar todos los servicios de cultivos concretos para asegurar el registro en el Singleton (US-009) ---
from python_forestacion.servicios.cultivos.pino_service import PinoService
from python_forestacion.servicios.cultivos.olivo_service import OlivoService
from python_forestacion.servicios.cultivos.lechuga_service import LechugaService
from python_forestacion.servicios.cultivos.zanahoria_service import ZanahoriaService


# --- Importaciones de Excepciones ---
from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.persistencia_exception import PersistenciaException
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException

# ----------------- Funciones de Inicialización -----------------


def inicializar_sistema() -> tuple[FincasService, TrabajadorService, RegistroForestalService, Plantacion, Optional[Trabajador], RegistroForestal]:
    """
    Inicializa todos los servicios, crea el escenario de negocio si no existe (US-001 a US-007).
    Se encarga de cargar un RegistroForestal o crearlo si no existe.
    """
    
    # Singleton: Obtener instancia (US-TECH-001)
    _ = CultivoServiceRegistry.get_instance() 
    
    # Servicios
    trabajador_service = TrabajadorService()
    tierra_service = TierraService()
    registro_forestal_service_instancia = RegistroForestalService("RegistroSimulacion") 
    fincas_service = FincasService(registro_forestal_service_instancia)
    plantacion_service = fincas_service._plantacion_service 
    
    plantacion: Optional[Plantacion] = None
    registro: Optional[RegistroForestal] = None
    primer_trabajador: Optional[Trabajador] = None

    try:
        # Intento cargar el registro (US-022)
        registro = RegistroForestalService.leer_registro("RegistroSimulacion") 
        plantacion = registro.get_plantacion()
        primer_trabajador = plantacion.get_trabajadores()[0] if plantacion.get_trabajadores() else None
        
        print(f"\n[PERSISTENCIA]: Estado cargado exitosamente desde {registro_forestal_service_instancia._ruta_archivo}")
        fincas_service.add_finca(registro) 
        
    except PersistenciaException:
        # --- CREACIÓN DE ESCENARIO (Si falla la carga) ---
        print("\n" + "=" * 70)
        print(" SISTEMA DE GESTION FORESTAL - PATRONES DE DISENO".center(70))
        print("=" * 70)
        
        print("\n" + "-" * 70)
        print(" PATRON SINGLETON: Inicializando CultivoServiceRegistry".center(70))
        print("-" * 70)
        print("[OK] CultivoServiceRegistry inicializado (Singleton)")
        
        print("\n" + "-" * 70)
        print(" CREACION DE FINCA Y PLANTACION (US-001 a US-003)".center(70))
        print("-" * 70)

        # 1. Creación de Terreno y Plantación
        terreno = tierra_service.crear_tierra_con_plantacion(
            id_padron=1,
            superficie=10000.0,
            domicilio="Agrelo, Mendoza",
            nombre_plantacion="El Olivar Dorado",
            agua_inicial=1500.0
        )
        plantacion = terreno.get_finca()
        
        # 2. Plantar cultivos (US-004 a US-007) - PATRON FACTORY METHOD
        print("\n2. Plantando cultivos (PATRON FACTORY METHOD)...")
        try:
            plantacion_service.plantar(plantacion, "Pino", 5)      # 5 * 2.0 = 10 m²
            plantacion_service.plantar(plantacion, "Olivo", 5)     # 5 * 3.0 = 15 m²
            plantacion_service.plantar(plantacion, "Lechuga", 20)  # 20 * 0.10 = 2 m²
            plantacion_service.plantar(plantacion, "Zanahoria", 10) # 10 * 0.15 = 1.5 m²
            print(f"[OK] Plantados 40 cultivos. Superficie ocupada: {plantacion.get_superficie_ocupada()} m²")
        
        except Exception as e:
            import traceback
            print(f"\n[ERROR FATAL INESPERADO]: {e}")
            # CRÍTICO: Imprimir el traceback completo para depurar el error 'variedad'
            traceback.print_exc() 
            # Es importante que el programa no continúe después de este error fatal
            exit() # Salir del programa

        # 3. Crear Registro Forestal (US-003)
        # ESTE BLOQUE DEBE ESTAR AL MISMO NIVEL DE INDENTACIÓN QUE EL try/except DE PLANTACION
        registro = RegistroForestal(
            id_padron=1,
            tierra=terreno,
            plantacion=plantacion,
            propietario="RegistroSimulacion",
            avaluo=50309233.55
        )
        fincas_service.add_finca(registro)
        print(f"[OK] Registro Forestal creado para {registro.get_propietario()}")

        # 4. Asignar trabajadores y obtener el primero para la simulación
        trabajadores_simulacion = inicializar_trabajadores(trabajador_service)
        plantacion.set_trabajadores(trabajadores_simulacion)
        primer_trabajador = trabajadores_simulacion[0] if trabajadores_simulacion else None
        
        # 5. Guardar el estado inicial (US-021)
        registro_forestal_service_instancia.persistir(registro)
        
    print(f"\n--- ESTADO INICIAL: Plantación '{plantacion.get_nombre()}' ({len(plantacion.get_cultivos())} cultivos) ---")
    
    return fincas_service, trabajador_service, registro_forestal_service_instancia, plantacion, primer_trabajador, registro

# ----------------- FUNCIONES DE INICIALIZACIÓN DE TRABAJADORES -----------------

def inicializar_trabajadores(trabajador_service: TrabajadorService) -> List[Trabajador]:
    """Crea los trabajadores y asigna tareas para la simulación."""
    fecha_hoy = date.today()
    
    # Tareas (US-014)
    # IDs se asignan automáticamente en la clase Tarea si está bien implementada
    tareas_asignadas_carlos = [
        Tarea(nombre="Desmalezar", descripcion="Limpieza de malezas", fecha_programada=fecha_hoy), 
        Tarea(nombre="Abonar", descripcion="Aplicar fertilizante", fecha_programada=fecha_hoy), 
        Tarea(nombre="Marcar surcos", descripcion="Preparar terreno", fecha_programada=fecha_hoy),
    ]
    
    # Trabajador Carlos (US-014)
    carlos = Trabajador(
        dni=43888734, 
        nombre="Carlos Perez", 
        tareas=tareas_asignadas_carlos.copy() # Defensive copy
    )
    
    # Trabajador Maria
    maria = Trabajador(
        dni=40222333,
        nombre="Maria Lopez",
        tareas=[] # Sin tareas, solo para demostrar apto
    )
    
    # Asignar apto médico a María (para que figure CON apto en el reporte final)
    trabajador_service.asignar_apto_medico(
        trabajador=maria,
        apto=True,
        fecha_emision=fecha_hoy,
        observaciones="Apto para todo tipo de tareas."
    )
    
    return [carlos, maria]

# ----------------- LÓGICA DE SIMULACIÓN Y NEGOCIO -----------------

def ejecutar_simulacion(fincas_service: FincasService, trabajador_service: TrabajadorService, plantacion: Plantacion, carlos: Trabajador):
    """
    Ejecuta las operaciones concurrentes y la lógica de negocio (US-010 a US-020).
    """
    
    hilos_concurrencia = []
    fecha_simulacion = date.today()
    
    try:
        # ==================== RIEGO AUTOMÁTICO (PATRON OBSERVER) ====================
        
        print("\n" + "-" * 70)
        print(" SISTEMA DE RIEGO AUTOMATICO (PATRON OBSERVER)".center(70))
        print("-" * 70)

        # 1. Inicializar y Arrancar Hilos (US-010, US-011, US-012)
        sensor_temp = TemperaturaReaderTask()
        sensor_humedad = HumedadReaderTask()
        riego_callback = lambda: fincas_service._plantacion_service.regar(plantacion)
        controlador = ControlRiegoTask(sensor_temp, sensor_humedad, riego_callback)
        
        hilos_concurrencia.extend([sensor_temp, sensor_humedad, controlador])
        
        print("\n1. Iniciando sensores y control automatico...")
        for hilo in hilos_concurrencia:
            hilo.start()
        
        print("[OK] Hilos iniciados. Simulando 10 segundos...")
        print("\n================ INICIANDO SIMULACIÓN CONCURRENTE (10 SEGUNDOS) ================")
        time.sleep(10) # Esperar 10 segundos para ver lecturas y riego automático
        
        # ==================== GESTIÓN DE TRABAJADORES (US-014 a US-017) ====================

        print("\n" + "-" * 70)
        print(" GESTION DE TRABAJADORES".center(70))
        print("-" * 70)

        herramienta_pala = Herramienta(nombre="Pala", descripcion="Pala forestal", certificacion_hs=True)

        # 2. Intentando trabajar SIN apto medico (US-016)
        print("\n2. Intentando trabajar SIN apto medico...")
        # El trabajador_service.trabajar ya imprime el mensaje de error si no tiene apto
        trabajador_service.trabajar(carlos, fecha=fecha_simulacion, util=herramienta_pala) 
        
        # 3. Asignando apto medico (US-015)
        print("\n3. Asignando apto medico...")
        apto = trabajador_service.asignar_apto_medico(
            trabajador=carlos,
            apto=True,
            fecha_emision=fecha_simulacion,
            observaciones="Estado de salud: excelente"
        )
        print(f"[OK] Apto medico asignado a {carlos.get_nombre()}. Estado: {apto.esta_apto()}")
        
        # 4. Trabajando CON apto medico (US-016)
        print("\n4. Trabajando CON apto medico...")
        trabajador_service.trabajar(carlos, fecha=fecha_simulacion, util=herramienta_pala) # Debería imprimir las tareas en orden descendente

        # ==================== OPERACIONES DE NEGOCIO (COSECHA) ====================

        print("\n" + "-" * 70)
        print(" COSECHA Y EMPAQUETADO (US-020)".center(70))
        print("-" * 70)
        
        # 5. Cosechar Pinos y Empaquetar (US-020)
        print("\n1. Cosechando Pinos...")
        caja_pinos = fincas_service.cosechar_y_empaquetar(Pino)
        # La impresión de la caja y el contenido debe estar en Paquete.mostrar_contenido_caja()
        # La superficie liberada se muestra en el servicio/método de cosecha, no aquí.
        if caja_pinos.get_cantidad() > 0:
            print(f"[OK] Cosechados {caja_pinos.get_cantidad()} Pino(s).") 
            caja_pinos.mostrar_contenido_caja()
        else:
            print("[INFO] No se cosecharon Pinos.")

        # 6. Cosechar Lechugas y Empaquetar (US-020)
        print("\n2. Cosechando Lechugas...")
        caja_lechugas = fincas_service.cosechar_y_empaquetar(Lechuga)
        # La impresión de la caja y el contenido debe estar en Paquete.mostrar_contenido_caja()
        # La superficie liberada se muestra en el servicio/método de cosecha, no aquí.
        if caja_lechugas.get_cantidad() > 0:
            print(f"[OK] Cosechados {caja_lechugas.get_cantidad()} Lechuga(s).")
            caja_lechugas.mostrar_contenido_caja()
        else:
            print("[INFO] No se cosecharon Lechugas.")
        
        # Final de la simulación
        print(f"\n[INFO] Cultivos restantes: {len(plantacion.get_cultivos())}")
        
    except ForestacionException as e:
        print(f"\n[ERROR CONTROLADO]: Fallo en la simulación: {e.get_user_message()}")
    except Exception as e:
        print(f"\n[ERROR CRÍTICO]: Falló la simulación: {e}")
    finally:
        # ==================== DETENCIÓN SEGURA (US-013) ====================
        print("\n================ DETENIENDO SIMULACIÓN CONCURRENTE (US-013) ================")
        
        for hilo in hilos_concurrencia:
            if hilo.is_alive():
                hilo.detener() # Asumo que implementaste .detener() en tus tareas
                hilo.join(timeout=THREAD_JOIN_TIMEOUT) 
        
        print("[OK] Todos los hilos se han detenido de forma segura.")


def guardar_y_finalizar(registro: RegistroForestal, registro_service_instancia: RegistroForestalService, fincas_service: FincasService):
    """
    Guarda el estado final y muestra el resumen completo del RegistroForestal (US-021, US-023).
    """
    
    plantacion = registro.get_plantacion()
    
    # ==================== RIEGO MANUAL Y REPORTE (PATRON STRATEGY) ====================
    
    print("\n" + "-" * 70)
    print(" RIEGO MANUAL (PATRON STRATEGY) Y REPORTE".center(70))
    print("-" * 70)
    
    # 1. Riego manual para actualizar estado y aplicar Strategy (US-008)
    print("\n1. Regando plantacion manualmente...")
    try:
        fincas_service._plantacion_service.regar(plantacion)
        print(f"[OK] Riego completado en '{plantacion.get_nombre()}'")
    except ForestacionException as e:
        print(f"[ERROR]: Fallo en el riego manual: {e.get_user_message()}")
    
    # 2. Persistencia y Reporte (US-021, US-023)
    print("\n" + "-" * 70)
    print(" PERSISTENCIA Y AUDITORIA".center(70))
    print("-" * 70)
    
    # Guardar el estado final (US-021)
    registro_service_instancia.persistir(registro)
    
    # Mostrar datos del registro completo (US-023)
    registro_service_instancia.mostrar_datos(registro)
    
    print("\n[PERSISTENCIA]: Estado del sistema guardado y reporte final generado.")
    
    # ==================== RESUMEN DE PATRONES ====================
    
    print("\n" + "=" * 70)
    print(" RESUMEN COMPLETADO EXITOSAMENTE".center(70))
    print("=" * 70)
    print("  [OK] SINGLETON   - CultivoServiceRegistry (instancia unica)")
    print("  [OK] FACTORY     - Creacion de cultivos")
    print("  [OK] OBSERVER    - Sistema de sensores y eventos")
    print("  [OK] STRATEGY    - Algoritmos de absorcion de agua")
    print("=" * 70)
    print("\n¡Ejecución finalizada con éxito! El estado final ha sido guardado.")

if __name__ == "__main__":
    # --- Ejecución principal del programa ---
    try:
        # La función inicializar_sistema ahora devuelve la instancia del servicio de registro
        fincas_service, trabajador_service, registro_service_instancia, plantacion, carlos, registro_completo = inicializar_sistema()
        
        # Verificamos que se haya inicializado todo correctamente
        if plantacion and registro_completo and carlos:
            ejecutar_simulacion(fincas_service, trabajador_service, plantacion, carlos)
            guardar_y_finalizar(registro_completo, registro_service_instancia, fincas_service)
        else:
            print("[ERROR FATAL]: El sistema no se pudo inicializar correctamente. Saliendo.")

    except ForestacionException as e:
        print(f"\n[FALLO DE INICIO]: El sistema no pudo arrancar debido a un error: {e.get_user_message()}")
    except Exception as e:
        print(f"\n[ERROR FATAL INESPERADO]: {e}")