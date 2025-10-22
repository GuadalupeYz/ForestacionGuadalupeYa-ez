# python_forestacion/entidades/cultivos/cultivo.py

from abc import ABC, abstractmethod
from typing import Optional, TYPE_CHECKING, Any 

if TYPE_CHECKING:
    from python_forestacion.patrones.strategy.absorcion_agua_strategy import EstrategiaAbsorcion

class Cultivo(ABC):
    """Clase base abstracta para todos los cultivos."""
    
    # CRÍTICO: **kwargs debe ser el último argumento.
    def __init__(self, nombre: str, superficie: float, agua_inicial: float, **kwargs):
        self._nombre = nombre
        self._superficie = superficie
        self._agua = agua_inicial 
        self._id: Optional[int] = None
        self._estrategia: Optional['EstrategiaAbsorcion'] = None
        self._esta_plantado = False 
        self._fase_crecimiento = 0

        # IMPORTANTE: Aquí se descartan los kwargs sobrantes (como 'variedad').
        # Si NO consumes el 'variedad' en Olivo ni en Arbol, aquí se descartaría finalmente.
        
        # Consumir (o simplemente ignorar) cualquier argumento restante en kwargs.
        # Si Cultivo hereda de ABC, su padre es 'object'. 
        # object.__init__() NO acepta **kwargs.
        # Por lo tanto, cualquier cosa que quede en kwargs DEBE ser vaciada aquí.
        if kwargs:
            # print(f"[DEBUG]: Argumentos sobrantes descartados en Cultivo: {kwargs.keys()}") # Opcional para depuración
            kwargs.clear() # ¡Esta es la clave! Vaciar el diccionario para que no cause TypeError.

    # --- Getters/Setters esenciales:
    def get_edad_anios(self) -> int:
        # ESTE MÉTODO DEBE ESTAR EN ARBOL, NO EN CULTIVO.
        # Si está aquí, causará confusión.
        # Para compatibilidad temporal, devuelve un valor por defecto.
        # Pero a la larga, debe eliminarse de Cultivo.
        return getattr(self, '_edad_anios', 0) 
    
    def get_nombre(self) -> str:
        return self._nombre

    def get_agua(self) -> float:
        return self._agua
    
    def set_agua(self, cantidad: float):
        self._agua = cantidad
        
    def get_superficie(self) -> float: 
        return self._superficie
        
    def set_id(self, id_val: int): 
        self._id = id_val
        
    def get_id(self) -> Optional[int]: 
        return self._id
    
    # Métodos de Estrategia (US-008):
    def set_estrategia(self, estrategia: 'EstrategiaAbsorcion'): 
        self._estrategia = estrategia
        
    def get_estrategia(self) -> 'EstrategiaAbsorcion':
        if not self._estrategia:
            raise AttributeError(f"El cultivo {self._nombre} no tiene estrategia de absorción asignada.")
        return self._estrategia

    # Método abstracto:
    @abstractmethod
    def __str__(self) -> str:
        pass