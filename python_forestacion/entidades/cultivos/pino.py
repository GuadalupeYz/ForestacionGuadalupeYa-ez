from .arbol import Arbol
from python_forestacion.constantes import SUPERFICIE_PINO, AGUA_INICIAL_PINO

class Pino(Arbol):
    """Cultivo concreto: Pino (US-005)."""
    def __init__(self, variedad: str = None, altura_metros: float = 0.0, edad_anios: int = 0):  # ← Cambiar _init_ por __init__
        super().__init__(  # ← Cambiar _init_ por __init__
            nombre="Pino",
            altura_metros=altura_metros,
            edad_anios=edad_anios,
            superficie=SUPERFICIE_PINO,
            agua_inicial=AGUA_INICIAL_PINO
        )
        self._variedad = variedad  # atributo específico de Pino
    
    def __str__(self) -> str:  # ← Cambiar _str_ por __str__
        return f"Pino (Edad: {self.get_edad_anios()} años, Altura: {self.get_altura()} m, Variedad: {self._variedad})"
    
    def get_variedad(self) -> str:
        return self._variedad