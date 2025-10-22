# python_forestacion/entidades/terrenos/plantacion.py

from python_forestacion.entidades.cultivos.cultivo import Cultivo # Asumo que Cultivo está correctamente definido
from python_forestacion.constantes import AGUA_DEFAULT_PLANTACION
from .tierra import Tierra # Asumo que Tierra se importa de forma relativa
from typing import List, Any, Optional
# No se necesita importar CultivoServiceRegistry aquí, solo en los servicios

class Plantacion:
    """Entidad que representa una plantación agrícola."""
    
    # CRÍTICO: La firma debe coincidir con la llamada de TierraService y agregar 'agua_inicial'
    def __init__(self, 
                 id_padron: int, 
                 superficie: float, 
                 domicilio: str, 
                 nombre_plantacion: str,
                 agua_inicial: float # <-- ARGUMENTO FALTANTE AHORA AGREGADO
                 ):
        
        # 1. Inicializar atributos
        self._id: int = id_padron
        self._nombre: str = nombre_plantacion
        self._superficie: float = superficie
        self._cultivos: List[Any] = [] 
        
        # 2. Inicializar Tierra (usa los argumentos que ya pasamos)
        # Nota: La Plantacion puede contener una referencia a Tierra, pero la Tierra
        # debería crearse con la Plantacion dentro del servicio. Aquí, la creamos 
        # directamente si el servicio así lo dicta.
        # CRÍTICO: El constructor de Tierra solo debe aceptar id_padron, superficie, domicilio.
        self._tierra: Tierra = Tierra(id_padron, superficie, domicilio) 
        
        # 3. Inicializar Agua
        self._agua_disponible: float = agua_inicial # Usamos el valor pasado

    # --- Getters ---
    
    def get_tierra(self) -> Tierra: 
        return self._tierra
        
    def get_cultivos(self) -> List[Any]: 
        return self._cultivos
        
    def add_cultivo(self, cultivo: Any): 
        self._cultivos.append(cultivo)
        
    def get_nombre(self) -> str:
        return self._nombre
        
    def get_agua_disponible(self) -> float: 
        return self._agua_disponible
        
    def get_superficie(self) -> float:
        return self._superficie
        
    # --- Setters/Mutators ---
        
    def set_agua_disponible(self, agua: float): 
        self._agua_disponible = agua
        
    def set_tierra(self, tierra: Tierra):
        self._tierra = tierra

    # --- Métodos de Negocio ---
    
    def get_superficie_maxima(self) -> float:
        """Retorna la superficie máxima total de la Plantación (la de la Tierra)."""
        # Debe devolver su propia superficie, que es la misma que la de la tierra.
        return self._superficie 

    def get_superficie_ocupada(self) -> float:
        """Calcula y retorna la suma de las superficies de todos los cultivos."""
        # Asumo que cada cultivo tiene un método get_superficie()
        return sum(cultivo.get_superficie() for cultivo in self._cultivos)

    def get_superficie_disponible(self) -> float:
        """Calcula y retorna la superficie libre."""
        return self.get_superficie_maxima() - self.get_superficie_ocupada()
        
    def get_id(self) -> int: 
        return self._id
        
    # Asumo que necesitas este método para asignarle trabajadores en main.py
    def get_trabajadores(self) -> List[Any]:
        # Si tienes trabajadores en Plantacion, debes inicializarlos y retornarlos.
        # Si no, asumo que los guardas en la Tierra o en un atributo.
        # Por ahora, devuelvo una lista vacía o asumo un atributo _trabajadores:
        if not hasattr(self, '_trabajadores'):
            self._trabajadores = []
        return self._trabajadores
        
    def set_trabajadores(self, trabajadores: List[Any]):
        self._trabajadores = trabajadores