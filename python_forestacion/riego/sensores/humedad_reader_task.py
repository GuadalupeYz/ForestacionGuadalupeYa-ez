import threading
import time
import random
from python_forestacion.patrones.observer.observable import Observable # RUTA CORRECTA
from python_forestacion.patrones.observer.eventos.evento_sensor import EventoSensor # RUTA CORRECTA
from python_forestacion.constantes import TIEMPO_LECTURA_SENSOR

class HumedadReaderTask(Observable[EventoSensor], threading.Thread):
    """Simula un sensor de humedad, notifica a los observadores (US-011)."""
    
    def __init__(self):
        Observable.__init__(self)
        threading.Thread.__init__(self, daemon=True)
        self._running = True
        self._lectura_actual = 50.0 

    def run(self):
        print(f"[SENSOR HUMEDAD]: Sensor de humedad iniciado.")
        while self._running:
            self._lectura_actual = round(random.uniform(35.0, 65.0), 1)
            evento = EventoSensor("humedad", self._lectura_actual)
            self.notify_observers(evento)
            print(f"[SENSOR HUMEDAD]: Lectura de {self._lectura_actual}%. Notificando...")
            time.sleep(TIEMPO_LECTURA_SENSOR * 1.5) 
        
        print("[SENSOR HUMEDAD]: Sensor detenido.")

    def stop(self):
        self._running = False