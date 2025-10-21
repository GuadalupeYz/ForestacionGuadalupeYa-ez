from typing import List, Generic, TypeVar
from abc import ABC
# Importar la interfaz Observer
from .observer import Observer 

# T es el tipo de dato del evento que se notifica
T = TypeVar('T') 

class Observable(Generic[T], ABC):
    """Clase base para los sujetos observables (sensores) (US-010, US-011)."""
    
    def __init__(self):
        # Ahora usa la clase Observer importada
        self._observers: List[Observer[T]] = [] 

    def add_observer(self, observer: Observer[T]):
        """Registra un observador."""
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer: Observer[T]):
        """Elimina un observador."""
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self, evento: T):
        """Notifica a todos los observadores registrados con el evento T."""
        for observer in self._observers:
            observer.update(self, evento)