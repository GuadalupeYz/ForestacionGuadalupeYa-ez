from .arbol import Arbol
from python_forestacion.constantes import SUPERFICIE_PINO, AGUA_INICIAL_PINO

class Pino(Arbol):
    """Cultivo concreto: Pino (US-005)."""
    
    def __init__(self, variedad: str, altura: float):
        super().__init__("Pino", SUPERFICIE_PINO, AGUA_INICIAL_PINO)
        self._variedad = variedad
        self._altura = altura # En metros

    def get_variedad(self) -> str: return self._variedad
    def get_altura(self) -> float: return self._altura

    def __str__(self) -> str:
        return f"Pino (Variedad: {self._variedad}, Altura: {self._altura:.2f}m)"