"""
Archivo integrador generado automaticamente
Directorio: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/patrones/observer
Fecha: 2025-10-22 12:40:53
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/patrones/observer/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: observable.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/patrones/observer/observable.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/3: observer.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/patrones/observer/observer.py
# ================================================================================

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

