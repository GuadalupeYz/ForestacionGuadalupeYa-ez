from abc import ABC, abstractmethod
from typing import Optional, TYPE_CHECKING
from python_forestacion.constantes import SUPERFICIE_PINO, AGUA_INICIAL_PINO

# Importamos la interfaz del Patrón Strategy usando TYPE_CHECKING
# Esto es CRÍTICO para evitar dependencias circulares y warnings.
if TYPE_CHECKING:
    from python_forestacion.patrones.strategy.absorcion_agua_strategy import EstrategiaAbsorcion

class Cultivo(ABC):
    """Clase base abstracta para todos los cultivos (US-004 a US-007)."""

    def __init__(self, nombre: str, superficie: float, agua_inicial: int):
        self._id: Optional[int] = None
        self._nombre = nombre
        self._superficie = superficie
        self._agua = agua_inicial
        # Interfaz del Patrón Strategy (US-008)
        self._estrategia: Optional['EstrategiaAbsorcion'] = None 
        self._id = 0 # O genera un ID
        self._agua_actual = agua_inicial # Para el riego
        self._estrategia_riego: Optional[EstrategiaAbsorcion] = None # Si usas Strategy aquí

    def get_superficie(self) -> float: return self._superficie
    def get_agua(self) -> int: return self._agua
    def set_agua(self, valor: int): self._agua = valor
    def set_id(self, id_val: int): self._id = id_val
    def get_id(self) -> Optional[int]: return self._id
    
    # Método esencial para el Factory (US-008)
    def set_estrategia(self, estrategia: 'EstrategiaAbsorcion'): 
        self._estrategia = estrategia
        
    def get_estrategia(self) -> 'EstrategiaAbsorcion':
        if not self._estrategia:
            raise AttributeError(f"El cultivo {self._nombre} no tiene estrategia de absorción asignada.")
        return self._estrategia

    @abstractmethod
    def __str__(self) -> str:
        pass

