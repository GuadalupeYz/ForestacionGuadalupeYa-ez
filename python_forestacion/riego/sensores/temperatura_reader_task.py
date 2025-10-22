import threading
import time
import random
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.patrones.observer.eventos.evento_sensor import EventoSensor
from python_forestacion.constantes import TIEMPO_LECTURA_SENSOR

class TemperaturaReaderTask(Observable[EventoSensor], threading.Thread):
    """Simula un sensor de temperatura, notifica a los observadores (US-010)."""
    
    def __init__(self, controlador):
        Observable.__init__(self)
        threading.Thread.__init__(self, daemon=True)
        self._running = True
        self._lectura_actual = 20.0
        self._controlador = controlador
    
    def run(self):
        """Método principal del hilo - ejecuta el ciclo de lectura"""
        print(f"[SENSOR TEMP]: Sensor de temperatura iniciado.")
        while self._running:
            # Leer temperatura simulada
            self._lectura_actual = round(random.uniform(18.0, 32.0), 1)
            
            # Crear evento y notificar
            evento = EventoSensor("temperatura", self._lectura_actual)
            self.notify_observers(evento)
            
            print(f"[SENSOR TEMP]: Lectura de {self._lectura_actual}°C. Notificando...")
            time.sleep(TIEMPO_LECTURA_SENSOR)
        
        print("[SENSOR TEMP]: Sensor detenido.")
    
    def detener(self):
        """Detiene el hilo de forma segura"""
        self._running = False
    
    def leer_temperatura(self):
        """Devuelve la última lectura de temperatura"""
        return self._lectura_actual