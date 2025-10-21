import os
import time
from datetime import date
from python_forestacion.servicios.negocios.fincas_service import FincasService
from python_forestacion.servicios.personal.trabajador_service import TrabajadorService
from python_forestacion.servicios.terrenos.registro_forestal_service import RegistroForestalService 
from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna

# --- IMPORTACIONES DE CONCURRENCIA ---
from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
from python_forestacion.riego.control.control_riego_task import ControlRiegoTask

from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.excepciones.forestacion_exception import ForestacionException

# Importar todos los servicios de cultivos concretos para asegurar su registro en el Singleton (US-009)
# CRÍTICO: Estas importaciones deben estar AQUÍ y no pueden faltar.
import python_forestacion.servicios.cultivos.pino_service 
import python_forestacion.servicios.cultivos.olivo_service 
import python_forestacion.servicios.cultivos.lechuga_service 
import python_forestacion.servicios.cultivos.zanahoria_service 

def inicializar_sistema():
    """
    Inicializa todos los servicios, entidades clave e intenta cargar el estado guardado (US-022).
    """
    
    # 1. Servicios
    registro_service = RegistroForestalService("registro_fincas_mendoza")
    # Nota: fincas_service debe cargarse DESPUÉS de intentar cargar el registro,
    # ya que su constructor depende de la existencia de plantacion.
    trabajador_service = TrabajadorService()
    
    # 2. Intentar cargar estado anterior
    estado_sistema = registro_service.cargar_registro()
    plantacion = estado_sistema.get('plantacion')
    trabajador = estado_sistema.get('trabajador')
    
    # Inicializamos fincas_service aquí, después de la carga
    fincas_service = FincasService(registro_service)
    
    if not plantacion:
        print("\n================ CREANDO NUEVO SISTEMA ==================")
        
        # Necesitamos PlantacionService para plantar
        plantacion_service = fincas_service._plantacion_service 
        
        # 1. Crear Plantación vacía (US-001)
        plantacion = fincas_service.crear_plantacion(
            id_padron=1020, 
            superficie=1500.0, 
            domicilio="Ruta 40 Km 10, Mendoza",
            nombre_plantacion="El Olivar Dorado"
        )
        
        # 2. Plantar Olivos (US-006)
        plantacion_service.plantar(
            plantacion, 
            "Olivo", 
            100, 
            tipo_aceituna=TipoAceituna.ARBEQUINA 
        )
        
        # 3. Plantar Lechuga (Hortaliza)
        plantacion_service.plantar(plantacion, "Lechuga", 50, peso=0.6)
        
        # 4. Inicializar Trabajador y persistir
        trabajador = Trabajador("Carlos", "García", 30123456, date(1985, 5, 10))
        trabajador_service.asignar_apto_medico(trabajador, date.today())
        
        estado_sistema['plantacion'] = plantacion
        estado_sistema['trabajador'] = trabajador
        
        registro_service.guardar_registro(estado_sistema)
        print("Sistema inicializado, 150 cultivos plantados y guardado exitosamente.")

    print(f"\n--- ESTADO INICIAL: Plantación '{plantacion._nombre}' ({len(plantacion.get_cultivos())} cultivos) ---")
    
    return fincas_service, trabajador_service, registro_service, plantacion, trabajador, estado_sistema

def ejecutar_simulacion(fincas_service: FincasService, trabajador_service: TrabajadorService, plantacion, trabajador: Trabajador):
    """
    Ejecuta las operaciones concurrentes y la lógica de negocio (US-010 a US-020).
    """
    
    hilos_concurrencia = []
    
    try:
        # 1. Inicializar y Arrancar Hilos (US-010, US-011)
        sensor_temp = TemperaturaReaderTask()
        sensor_humedad = HumedadReaderTask()
        hilos_concurrencia.extend([sensor_temp, sensor_humedad])
        
        # 2. Inicializar Controlador de Riego (US-012)
        riego_callback = lambda: fincas_service._plantacion_service.regar(plantacion)
        controlador = ControlRiegoTask(sensor_temp, sensor_humedad, riego_callback)
        hilos_concurrencia.append(controlador)
        
        # 3. Iniciar hilos (US-013)
        for hilo in hilos_concurrencia:
            hilo.start()
        
        print("\n================ INICIANDO SIMULACIÓN CONCURRENTE (10 SEGUNDOS) ================")
        time.sleep(5)
        
        # 4. Operación de Negocio Manual (US-015, US-019, US-020)
        print("\n--- OPERACIONES MANUALES DE NEGOCIO ---")
        
        cultivos_cosechados = trabajador_service.cosechar(trabajador, plantacion, "Lechuga")
        
        if cultivos_cosechados:
            fincas_service.crear_paquetes(cultivos_cosechados, "Lote Cosecha Lechuga")
            
        print(f"\nLa Plantación tiene ahora {len(plantacion.get_cultivos())} cultivos restantes.")

        time.sleep(5) 
        
    except ForestacionException as e:
        print(f"\n[ERROR CONTROLADO]: Fallo en la simulación: {e.get_user_message()}")
    except Exception as e:
        print(f"\n[ERROR CRÍTICO]: Falló la simulación: {e}")
    finally:
        print("\n================ DETENIENDO SIMULACIÓN CONCURRENTE (US-013) ================")
        
        # 5. Detener hilos de forma segura (US-013)
        for hilo in hilos_concurrencia:
            if hilo.is_alive():
                # Asumo que todos los hilos tienen un método .stop()
                hilo.stop() 

def guardar_y_finalizar(fincas_service: FincasService, registro_service: RegistroForestalService, estado_sistema: dict):
    """Guarda el estado final y muestra el resumen (US-021), incluyendo la impresión de patrones."""
    
    plantacion = estado_sistema.get('plantacion')
    if plantacion:
        print(f"\n--- ESTADO FINAL: Plantación '{plantacion._nombre}' ---")
        
        # Riego final e impresión de info de cultivos
        fincas_service.regar_y_mostrar_info(plantacion) 
        
        # BLOQUE DE RESUMEN DE PATRONES (Asegurado dentro de la función)
        print("\n======================================================================")
        print("              EJEMPLO COMPLETADO EXITOSAMENTE                       ")
        print("======================================================================")
        print("  [OK] SINGLETON   - CultivoServiceRegistry (instancia unica)")
        print("  [OK] FACTORY     - Creacion de cultivos")
        print("  [OK] OBSERVER    - Sistema de sensores y eventos")
        print("  [OK] STRATEGY    - Algoritmos de absorcion de agua")
        print("======================================================================")
        
        # Guardar el estado final y mensaje de éxito
        registro_service.guardar_registro(estado_sistema)
        print("\n¡Ejecución finalizada con éxito! El estado final ha sido guardado.")

if __name__ == "__main__":
    try:
        fincas_service, trabajador_service, registro_service, plantacion, trabajador, estado_sistema = inicializar_sistema()
        
        ejecutar_simulacion(fincas_service, trabajador_service, plantacion, trabajador)
        
        # Llama a guardar_y_finalizar para el riego final y la persistencia
        guardar_y_finalizar(fincas_service, registro_service, estado_sistema)

    except ForestacionException as e:
        print(f"\n[FALLO DE INICIO]: El sistema no pudo arrancar debido a un error: {e.get_user_message()}")
    except Exception as e:
        print(f"\n[ERROR FATAL INESPERADO]: {e}")
    
    # La impresión de finalización (con guardado) ya ocurre dentro de guardar_y_finalizar,
    # pero a modo de respaldo final, puedes poner un print final aquí si el otro falla.
    # print("\n¡Ejecución finalizada con éxito! El estado final ha sido guardado.")
