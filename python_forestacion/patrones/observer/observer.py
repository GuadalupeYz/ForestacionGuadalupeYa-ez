from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Any

# T es el tipo de dato del evento que se notifica
T = TypeVar('T') 

class Observer(Generic[T], ABC):
    """Interfaz para los observadores (US-012)."""
    @abstractmethod
    def update(self, observable: Any, evento: T):
        """Método llamado por el observable para notificar un cambio."""
        pass