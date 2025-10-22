from python_forestacion.constantes import TipoOperacion
from .forestacion_exception import ForestacionException

class SuperficieInsuficienteException(ForestacionException):
    """Excepción lanzada cuando no hay suficiente superficie para la plantación (US-004)."""
    
    def __init__(self, tipo_cultivo: str, requerida: float, disponible: float):
        super().__init__(
            TipoOperacion.PLANTACION, 
            "SUPERFICIE_INSUF", 
            tipo=tipo_cultivo, 
            requerida=requerida, 
            disponible=disponible
        )