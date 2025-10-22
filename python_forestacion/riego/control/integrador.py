"""
Archivo integrador generado automaticamente
Directorio: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/riego/control
Fecha: 2025-10-22 10:21:44
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/riego/control/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: control_riego_task.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/riego/control/control_riego_task.py
# ================================================================================

import threading
import time
from typing import Callable, Any
from python_forestacion.patrones.observer.observable import Observer # RUTA CORRECTA
from python_forestacion.patrones.observer.eventos.evento_sensor import EventoSensor # RUTA CORRECTA
from python_forestacion.constantes import UMBRAL_TEMPERATURA, UMBRAL_HUMEDAD

class ControlRiegoTask(Observer[EventoSensor], threading.Thread):
    """Controlador de riego. Implementa Observer para reaccionar a los sensores (US-012)."""
    
    def __init__(self, sensor_temp: Any, sensor_humedad: Any, riego_callback: Callable[[], Any]):
        threading.Thread.__init__(self, daemon=True)
        self._running = True
        self._sensor_temp = sensor_temp
        self._sensor_humedad = sensor_humedad
        self._riego_callback = riego_callback
        self._activo = True
        self._ultima_temp = 0.0
        self._ultima_humedad = 0.0
        
        self._sensor_temp.add_observer(self)
        self._sensor_humedad.add_observer(self)

    def update(self, observable: Any, evento: EventoSensor):
        """Método de Observer: recibe las lecturas y chequea la condición de riego (US-012)."""
        if evento.get_tipo() == "temperatura":
            self._ultima_temp = evento.get_lectura()
        elif evento.get_tipo() == "humedad":
            self._ultima_humedad = evento.get_lectura()

        self._verificar_y_ejecutar_riego()

    def _verificar_y_ejecutar_riego(self):
        if self._ultima_temp > UMBRAL_TEMPERATURA and self._ultima_humedad < UMBRAL_HUMEDAD:
            print(f"\n[CONTROLADOR RIEGO]: ¡CONDICIÓN DE RIEGO DETECTADA!")
            print(f"  -> Temp: {self._ultima_temp}°C (>{UMBRAL_TEMPERATURA}°) | Hum: {self._ultima_humedad}% (<{UMBRAL_HUMEDAD}%)")
            
            try:
                self._riego_callback() 
            except Exception as e:
                print(f"[CONTROLADOR RIEGO ERROR]: Falló el riego: {e}")
            
            self._ultima_temp = 0.0
            self._ultima_humedad = 100.0
            time.sleep(1)

    def run(self):
        while self._activo:
            # lógica de riego
            pass

    def detener(self):
        self._activo = False


