# Contenido esperado en hortaliza.py

from .cultivo import Cultivo

class Hortaliza(Cultivo):
    """Clase base para todos los tipos de hortalizas."""
    def __init__(self, **kwargs):
        # Simplemente llama al constructor de la clase padre (Cultivo) 
        # y le pasa TODOS los argumentos restantes.
        super().__init__(**kwargs)
