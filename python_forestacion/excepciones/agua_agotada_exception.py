from .forestacion_exception import ForestacionException
from python_forestacion.constantes import TipoOperacion, AGUA_MINIMA_RIEGOS

class AguaAgotadaException(ForestacionException):
    """Excepción lanzada cuando el agua de la plantación es insuficiente para un riego (US-008)."""
    
    def __init__(self, agua_actual: int):
        super().__init__(
            TipoOperacion.RIEGO, 
            "AGUA_AGOTADA", 
            agua_actual=agua_actual, 
            minimo=AGUA_MINIMA_RIEGOS
        )