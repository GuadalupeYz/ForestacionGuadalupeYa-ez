
# La importación de Cultivo ahora debe funcionar:
from python_forestacion.entidades.cultivos.cultivo import Cultivo 
from python_forestacion.constantes import AGUA_DEFAULT_PLANTACION
from .tierra import Tierra
from typing import List, Any
# from python_forestacion.entidades.cultivos.cultivo import Cultivo # Asumo que esta entidad existe

class Plantacion:
    """Entidad que representa una plantación agrícola."""
    
    def __init__(self, nombre: str, tierra: Tierra):
        self._id = id
        self._nombre = nombre
        self._tierra = tierra
        self._cultivos: List[Any] = [] # Usamos Any para evitar referencias circulares
        self._agua_disponible = 5000 # Litros iniciales
        
    def get_tierra(self) -> Tierra: return self._tierra
    def get_cultivos(self) -> List[Any]: return self._cultivos
    def add_cultivo(self, cultivo: Any): self._cultivos.append(cultivo)
    
    # MÉTODO CRÍTICO: Debe devolver un número, no el objeto Tierra.
    def get_superficie_maxima(self) -> float: 
        # Asumo que Tierra tiene un método get_superficie() o un atributo _superficie
        return self._tierra.get_superficie() # O self._tierra._superficie 
        
    def get_agua_disponible(self) -> float: return self._agua_disponible
    def set_agua_disponible(self, agua: float): self._agua_disponible = agua