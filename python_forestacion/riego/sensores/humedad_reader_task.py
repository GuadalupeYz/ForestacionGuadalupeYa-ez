import threading
import time
import random
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.patrones.observer.eventos.evento_sensor import EventoSensor
from python_forestacion.constantes import TIEMPO_LECTURA_SENSOR


class HumedadReaderTask(Observable[EventoSensor], threading.Thread):
    """Simula un sensor de humedad, notifica a los observadores (US-011)."""
    
    def __init__(self):
        Observable.__init__(self)
        threading.Thread.__init__(self, daemon=True)
        self._running = True
        self._lectura_actual = 60.0

    def agregar_observador(self, observador):
      """Compatibilidad con ControlRiegoTask (Observer Pattern)."""
      self.add_observer(observador)


    def run(self):
        """Método principal del hilo - ejecuta el ciclo de lectura"""
        print("[SENSOR HUMEDAD]: Sensor de humedad iniciado.")
        while self._running:
            # Leer humedad simulada
            self._lectura_actual = round(random.uniform(35.0, 65.0), 1)

            # Crear evento y notificar
            evento = EventoSensor("humedad", self._lectura_actual)
            self.notify_observers(evento)

            print(f"[SENSOR HUMEDAD]: Lectura de {self._lectura_actual}% Notificando...")
            time.sleep(TIEMPO_LECTURA_SENSOR * 1.5)

        print("[SENSOR HUMEDAD]: Sensor detenido.")

    def detener(self):
        """Detiene el hilo de forma segura"""
        self._running = False

    def leer_humedad(self):
        """Devuelve la última lectura de humedad"""
        return self._lectura_actual
