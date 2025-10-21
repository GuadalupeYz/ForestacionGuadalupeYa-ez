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
AGUA_DEFAULT_PLANTACION = 50000
AGUA_MINIMA_RIEGOS = 1000 # Mínimo de agua para iniciar el riego automático

# --- Constantes de Simulación Concurrente ---
TIEMPO_LECTURA_SENSOR = 2.0 # Segundos
UMBRAL_TEMPERATURA = 25.0 # Grados Celsius
UMBRAL_HUMEDAD = 40.0 # Porcentaje

# --- Constantes de Absorción Estacional (NUEVAS LÍNEAS) ---
ABSORCION_VERANO = 20 # Litros extra de agua absorbida en verano (factor alto)
ABSORCION_INVIERNO = 5 # Litros extra de agua absorbida en invierno (factor bajo)

# ... (Todo el contenido anterior de constantes.py) ...

from enum import Enum

class TipoOperacion(Enum):
    """Tipos de operaciones para registrar y centralizar mensajes de error."""
    PLANTACION = "PLANTACIÓN"
    RIEGO = "RIEGO"
    COSECHA = "COSECHA"
    PERSISTENCIA = "PERSISTENCIA"
    CONCURRENCIA = "CONCURRENCIA"