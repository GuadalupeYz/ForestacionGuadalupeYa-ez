import threading
import time
import random
from python_forestacion.patrones.observer.observable import Observable # RUTA CORRECTA
from python_forestacion.patrones.observer.eventos.evento_sensor import EventoSensor # RUTA CORRECTA
from python_forestacion.constantes import TIEMPO_LECTURA_SENSOR

class TemperaturaReaderTask(Observable[EventoSensor], threading.Thread):
    """Simula un sensor de temperatura, notifica a los observadores (US-010)."""
    
    def __init__(self):
        Observable.__init__(self)
        threading.Thread.__init__(self, daemon=True)
        self._running = True
        self._lectura_actual = 20.0 

    def run(self):
        print(f"[SENSOR TEMP]: Sensor de temperatura iniciado.")
        while self._running:
            self._lectura_actual = round(random.uniform(18.0, 32.0), 1)
            evento = EventoSensor("temperatura", self._lectura_actual)
            self.notify_observers(evento)
            print(f"[SENSOR TEMP]: Lectura de {self._lectura_actual}°C. Notificando...")
            time.sleep(TIEMPO_LECTURA_SENSOR)
        
        print("[SENSOR TEMP]: Sensor detenido.")

    def stop(self):
        self._running = False