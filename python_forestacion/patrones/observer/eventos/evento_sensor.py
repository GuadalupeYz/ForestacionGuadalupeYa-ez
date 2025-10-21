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