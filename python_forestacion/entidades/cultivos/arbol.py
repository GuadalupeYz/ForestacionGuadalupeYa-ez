# En python_forestacion/entidades/cultivos/arbol.py

from .cultivo import Cultivo # Asumo que Arbol hereda de Cultivo

class Arbol(Cultivo):
    """Clase base para todos los tipos de árboles."""
    def __init__(self, nombre: str, edad: int, superficie: float, agua_inicial: float, **kwargs):
        super().__init__(nombre=nombre, superficie=superficie, agua_inicial=agua_inicial, **kwargs)
        self._edad = edad # ¡Esta línea es CRÍTICA para que _edad exista!

def get_edad(self) -> int:
        return self._edad
