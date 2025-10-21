from .hortaliza import Hortaliza
from python_forestacion.constantes import SUPERFICIE_LECHUGA, AGUA_INICIAL_LECHUGA

class Lechuga(Hortaliza):
    """Cultivo concreto: Lechuga (US-007)."""
    
    def __init__(self, peso: float = 0.5):
        super().__init__("Lechuga", SUPERFICIE_LECHUGA, AGUA_INICIAL_LECHUGA)
        self._peso = peso # En kg

    def get_peso(self) -> float: return self._peso

    def __str__(self) -> str:
        return f"Lechuga (Peso: {self._peso:.2f}kg)"