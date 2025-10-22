"""
Archivo integrador generado automaticamente
Directorio: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/patrones/observer/eventos
Fecha: 2025-10-22 10:21:44
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/patrones/observer/eventos/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: evento_plantacion.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/patrones/observer/eventos/evento_plantacion.py
# ================================================================================



# ================================================================================
# ARCHIVO 3/3: evento_sensor.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/patrones/observer/eventos/evento_sensor.py
# ================================================================================

from typing import Literal

# Definimos los valores literales (tipos fijos) que puede tomar el sensor.
SensorValue = Literal['temperatura'] | Literal['humedad']

class EventoSensor:
    """Clase DTO (Data Transfer Object) para los datos notificados por los sensores (US-010, US-011)."""

    def __init__(self, tipo_sensor: SensorValue, lectura: float):
        self._tipo_sensor = tipo_sensor
        self._lectura = lectura
        
    def get_tipo(self) -> SensorValue: 
        return self._tipo_sensor
        
    def get_lectura(self) -> float: 
        return self._lectura

