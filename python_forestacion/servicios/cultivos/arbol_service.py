# Contenido de python_forestacion/servicios/cultivos/arbol_service.py

# Usar importación RELATIVA para módulos dentro del mismo paquete 'cultivos'
from .cultivo_service import CultivoService 

class ArbolService(CultivoService):
    """
    Servicio base para todos los cultivos de tipo árbol (Pino, Olivo).
    """
    
    def __init__(self, estrategia_absorcion):
        super().__init__(estrategia_absorcion)

    def crecer(self, arbol, incremento_metros):
        """Lógica de crecimiento común a todos los árboles."""
        nueva_altura = arbol.get_altura_metros() + incremento_metros
        arbol.set_altura_metros(nueva_altura)
        
    pass