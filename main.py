import os
import time
from datetime import date
from typing import List, Optional

# --- Importaciones de Servicios ---
from python_forestacion.servicios.negocios.fincas_service import FincasService
from python_forestacion.servicios.personal.trabajador_service import TrabajadorService
from python_forestacion.servicios.terrenos.registro_forestal_service import RegistroForestalService
from python_forestacion.servicios.terrenos.tierra_service import TierraService
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry

# --- Importaciones de Entidades ---
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.entidades.personal.tarea import Tarea
from python_forestacion.entidades.personal.herramienta import Herramienta

# --- Importaciones de Riego (Observer) ---
from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
from python_forestacion.riego.control.control_riego_task import ControlRiegoTask
from python_forestacion.constantes import THREAD_JOIN_TIMEOUT

# --- Importaciones de Excepciones ---
from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.persistencia_exception import PersistenciaException

# -------------------- INICIALIZACIÓN DEL SISTEMA --------------------

def inicializar_sistema() -> tuple[FincasService, TrabajadorService, RegistroForestalService, Plantacion, Optional[Trabajador], RegistroForestal]:
    """Inicializa todos los servicios y crea la simulación base."""
    _ = CultivoServiceRegistry.get_instance()

    trabajador_service = TrabajadorService()
    tierra_service = TierraService()
    registro_service = RegistroForestalService("GuadalupeYañez")
    fincas_service = FincasService(registro_service)
    plantacion = None
    registro = None
    primer_trabajador = None

    try:
        registro = RegistroForestalService.leer_registro("GuadalupeYañez")
        plantacion = registro.get_plantacion()
        primer_trabajador = plantacion.get_trabajadores()[0] if plantacion.get_trabajadores() else None
        print(f"\n[PERSISTENCIA]: Estado cargado exitosamente desde {registro_service._ruta_archivo}")
        fincas_service.add_finca(registro)

    except PersistenciaException:
        print("\n" + "=" * 70)
        print(" SISTEMA DE GESTION FORESTAL - PATRONES DE DISEÑO ".center(70))
        print("=" * 70)

        print("\n" + "-" * 70)
        print(" PATRÓN SINGLETON: Inicializando servicios ".center(70))
        print("-" * 70)
        print("[REGISTRY]: CultivoServiceRegistry inicializado.")

                # --------------------------------------------------------------
        #   CREACIÓN DE TIERRA Y PLANTACIÓN
        # --------------------------------------------------------------
        print("\n" + "-" * 70)
        print("                   CREACIÓN DE TIERRA Y PLANTACIÓN                    ")
        print("-" * 70)

        try:
            tierra_service = TierraService()
            tierra = tierra_service.crear_tierra_con_plantacion(
                id_padron=1,
                superficie=12000.0,
                domicilio="Ruta Provincial 15, Luján de Cuyo, Mendoza",
                nombre_plantacion="El Olivar Dorado",
                agua_inicial=2000.0
            )
            plantacion = tierra.get_finca()
            print(f"[TIERRA]: Creada tierra Padrón #{tierra.get_id_padron()} en {tierra.get_domicilio()} ({tierra.get_superficie()} m²)")
            print(f"[PLANTACIÓN]: Creada '{plantacion.get_nombre()}' con {plantacion.get_agua_disponible()} L disponibles.")
            print("Plantación creada exitosamente.\n")

        except Exception as e:
            print(f"[ERROR FATAL]: {e}")

        print("\n" + "-" * 70)
        print(" PATRÓN FACTORY METHOD: Creación de cultivos ".center(70))
        print("-" * 70)
        plantacion_service = fincas_service._plantacion_service
        plantacion_service.plantar(plantacion, "Pino", 5)
        plantacion_service.plantar(plantacion, "Olivo", 5)
        plantacion_service.plantar(plantacion, "Lechuga", 20)
        plantacion_service.plantar(plantacion, "Zanahoria", 10)
        print(f"[OK] Se plantaron 40 cultivos en '{plantacion.get_nombre()}'.")
        print(f"[INFO] Superficie ocupada: {plantacion.get_superficie_ocupada()} m²")

        registro = RegistroForestal(
            id_padron=1,
            tierra=tierra,
            plantacion=plantacion,
            propietario="Guadalupe Yañez",
            avaluo=50309233.55
        )
        fincas_service.add_finca(registro)
        print(f"[OK] Registro Forestal creado para {registro.get_propietario()}.")

        trabajadores = inicializar_trabajadores(trabajador_service)
        plantacion.set_trabajadores(trabajadores)
        primer_trabajador = trabajadores[0]

        registro_service.persistir(registro)

    print(f"\n--- ESTADO INICIAL: Plantación '{plantacion.get_nombre()}' ({len(plantacion.get_cultivos())} cultivos) ---")
    return fincas_service, trabajador_service, registro_service, plantacion, primer_trabajador, registro

# -------------------- INICIALIZACIÓN DE TRABAJADORES --------------------

def inicializar_trabajadores(servicio: TrabajadorService) -> List[Trabajador]:
    hoy = date.today()
    tareas = [
        Tarea(nombre="Desmalezar", descripcion="Limpieza de malezas", fecha_programada=hoy),
        Tarea(nombre="Abonar", descripcion="Aplicar fertilizante", fecha_programada=hoy),
        Tarea(nombre="Marcar surcos", descripcion="Preparar terreno", fecha_programada=hoy)
    ]

    carlos = Trabajador(dni=43888734, nombre="Carlos Perez", tareas=tareas)
    maria = Trabajador(dni=40222333, nombre="Maria Lopez", tareas=[])

    servicio.asignar_apto_medico(maria, apto=True, fecha_emision=hoy, observaciones="Apto general.")
    return [carlos, maria]

# -------------------- SIMULACIÓN PRINCIPAL --------------------

def ejecutar_simulacion(fincas_service: FincasService, trabajador_service: TrabajadorService, plantacion: Plantacion, carlos: Trabajador):
    hilos = []
    fecha = date.today()

    try:
        print("\n" + "-" * 70)
        print(" SISTEMA DE RIEGO AUTOMÁTICO (PATRÓN OBSERVER) ".center(70))
        print("-" * 70)

        sensor_temp = TemperaturaReaderTask()
        sensor_hum = HumedadReaderTask()
        riego_callback = lambda: fincas_service._plantacion_service.regar(plantacion)

        controlador = ControlRiegoTask(sensor_temp, sensor_hum, riego_callback)
        hilos.extend([sensor_temp, sensor_hum, controlador])

        print("[INFO] Iniciando sensores y controlador...")
        for hilo in hilos:
            hilo.start()

        print("[OK] Sensores en ejecución. Simulando por 10 segundos...")
        time.sleep(10)

        print("\n" + "-" * 70)
        print(" GESTIÓN DE PERSONAL ".center(70))
        print("-" * 70)

        herramienta = Herramienta(nombre="Pala", descripcion="Pala forestal", certificacion_hs=True)
        print("\n[TEST] Intentando trabajar sin apto médico...")
        trabajador_service.trabajar(carlos, fecha, herramienta)

        print("\n[TEST] Asignando apto médico a Carlos...")
        apto = trabajador_service.asignar_apto_medico(carlos, apto=True, fecha_emision=fecha, observaciones="Buen estado de salud.")
        print(f"[OK] {carlos.get_nombre()} tiene apto médico: {apto.esta_apto()}")

        print("\n[TEST] Trabajando con apto médico...")
        trabajador_service.trabajar(carlos, fecha, herramienta)

    except ForestacionException as e:
        print(f"[ERROR CONTROLADO]: {e.get_user_message()}")
    except Exception as e:
        print(f"[ERROR CRÍTICO]: {e}")
    finally:
        print("\n================ DETENIENDO SIMULACIÓN CONCURRENTE (US-013) ================")
        for hilo in hilos:
            if hilo.is_alive():
                hilo.detener()
                hilo.join(timeout=THREAD_JOIN_TIMEOUT)
        print("[OK] Todos los hilos se han detenido correctamente.")

# -------------------- GUARDADO Y REPORTE FINAL --------------------

def guardar_y_finalizar(registro: RegistroForestal, servicio: RegistroForestalService, fincas_service: FincasService):
    plantacion = registro.get_plantacion()

    print("\n" + "-" * 70)
    print(" RIEGO MANUAL (PATRÓN STRATEGY) Y REPORTE ".center(70))
    print("-" * 70)
    try:
        fincas_service._plantacion_service.regar(plantacion)
        print(f"[OK] Riego completado en '{plantacion.get_nombre()}'.")
    except ForestacionException as e:
        print(f"[ERROR]: {e.get_user_message()}")

    print("\n" + "-" * 70)
    print(" PERSISTENCIA Y AUDITORÍA ".center(70))
    print("-" * 70)

    servicio.persistir(registro)
    servicio.mostrar_datos(registro)
    print("\n[PERSISTENCIA]: Estado del sistema guardado y reporte final generado.")

    print("\n" + "=" * 70)
    print(" EJEMPLO COMPLETADO EXITOSAMENTE ".center(70))
    print("=" * 70)
    print("  [OK] SINGLETON   - CultivoServiceRegistry (instancia única)")
    print("  [OK] FACTORY     - Creación de cultivos")
    print("  [OK] OBSERVER    - Sistema de sensores y eventos")
    print("  [OK] STRATEGY    - Algoritmos de absorción de agua")
    print("=" * 70)
    print("\n¡Ejecución finalizada con éxito! El estado final ha sido guardado.")

# -------------------- EJECUCIÓN PRINCIPAL --------------------

if __name__ == "__main__":
    try:
        fincas_service, trabajador_service, registro_service, plantacion, carlos, registro = inicializar_sistema()
        if plantacion and registro and carlos:
            ejecutar_simulacion(fincas_service, trabajador_service, plantacion, carlos)
            guardar_y_finalizar(registro, registro_service, fincas_service)
        else:
            print("[ERROR]: El sistema no se inicializó correctamente.")
    except Exception as e:
        print(f"[ERROR FATAL]: {e}")
