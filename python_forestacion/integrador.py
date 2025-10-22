"""
Archivo integrador generado automaticamente
Directorio: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion
Fecha: 2025-10-22 12:40:53
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: constantes.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/constantes.py
# ================================================================================

# --- Constantes para Persistencia ---
DIRECTORIO_DATA = "data"
EXTENSION_DATA = ".dat"

# --- Constantes para Concurrencia (threads) ---
THREAD_JOIN_TIMEOUT = 1.0 # Tiempo en segundos para esperar que los hilos terminen (1.0 segundo es un valor típico)
SENSOR_LECTURA_INTERVALO = 2 # Segundos entre lecturas de sensores
CONTROL_RIEGO_INTERVALO = 3 # Segundos entre chequeos del controlador de riego

# --- Constantes para Superficie (m²) ---
SUPERFICIE_PINO = 2.0
SUPERFICIE_OLIVO = 3.0
SUPERFICIE_LECHUGA = 0.1
SUPERFICIE_ZANAHORIA = 0.05

# --- Constantes para Agua Inicial (Litros) ---
AGUA_INICIAL_PINO = 100
AGUA_INICIAL_OLIVO = 80
AGUA_INICIAL_LECHUGA = 10
AGUA_INICIAL_ZANAHORIA = 5

# --- Constantes de Riego y Plantación ---
AGUA_DEFAULT_PLANTACION = 5000
AGUA_MINIMA_RIEGOS = 1000 # Mínimo de agua para iniciar el riego automático

# --- Constantes de Simulación Concurrente ---
TIEMPO_LECTURA_SENSOR = 2.0 # Segundos
UMBRAL_TEMPERATURA = 25.0 # Grados Celsius
UMBRAL_HUMEDAD = 40.0 # Porcentaje

# --- Constantes de Absorción Estacional (NUEVAS LÍNEAS) ---
ABSORCION_VERANO = 20 # Litros extra de agua absorbida en verano (factor alto)
ABSORCION_INVIERNO = 5 # Litros extra de agua absorbida en invierno (factor bajo)

# ... (Todo el contenido anterior de constantes.py) ...

# Archivo: python_forestacion/constantes.py (o donde esté TipoOperacion)
from enum import Enum

class TipoOperacion(Enum):
    """Tipos de operaciones para registrar y centralizar mensajes de error."""
    PLANTACION = "PLANTACIÓN"
    RIEGO = "RIEGO"
    COSECHA = "COSECHA"
    PERSISTENCIA = "PERSISTENCIA"
    CONCURRENCIA = "CONCURRENCIA"
    # --- ¡AGREGA O VERIFICA ESTO! ---
    CARGA = "CARGA"      # Necesario para la función leer_registro o from_deserialization_exception
    GUARDADO = "GUARDADO" # Si usas GUARDADO en persistir()
    LECTURA = "LECTURA"   # Si usas LECTURA en from_deserialization_exception
    # ---------------------------------

