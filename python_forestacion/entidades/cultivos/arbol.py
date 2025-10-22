from .cultivo import Cultivo

class Arbol(Cultivo):
    """Clase base para todos los tipos de árboles."""
    def __init__(self, nombre: str = None, **kwargs):  # ← Cambiar _init_ por __init__
        self._nombre = nombre
        self._altura_metros = kwargs.pop('altura_metros', 0.0)
        self._edad_anios = kwargs.pop('edad_anios', 0)
        nombre_cultivo = kwargs.pop('nombre', 'Árbol Base')
        superficie_cultivo = kwargs.pop('superficie', 0.0)
        agua_cultivo = kwargs.pop('agua_inicial', 0.0)
        super().__init__(  # ← Cambiar _init_ por __init__
            nombre=nombre_cultivo,
            superficie=superficie_cultivo,
            agua_inicial=agua_cultivo,
            **kwargs
        )
    
    def get_edad_anios(self) -> int:
        return self._edad_anios
    
    def get_altura(self) -> float:
        return self._altura_metros
    
    def get_edad(self) -> int:
        """Método de compatibilidad para evitar errores en Olivo.__str__"""
        return self._edad_anios