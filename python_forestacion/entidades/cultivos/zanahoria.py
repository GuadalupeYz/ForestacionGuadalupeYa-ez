from .hortaliza import Hortaliza
from python_forestacion.constantes import SUPERFICIE_ZANAHORIA, AGUA_INICIAL_ZANAHORIA

class Zanahoria(Hortaliza):
    """Cultivo concreto: Zanahoria (US-007)."""
    
    def __init__(self, longitud: float = 0.2):
        super().__init__("Zanahoria", SUPERFICIE_ZANAHORIA, AGUA_INICIAL_ZANAHORIA)
        self._longitud = longitud # En metros

    def get_longitud(self) -> float: return self._longitud

    def __str__(self) -> str:
        return f"Zanahoria (Longitud: {self._longitud:.2f}m)"