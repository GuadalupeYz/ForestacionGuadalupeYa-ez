# Importación CORREGIDA usando ruta relativa (..)
from ..absorcion_agua_strategy import EstrategiaAbsorcion 
from python_forestacion.entidades.cultivos.cultivo import Cultivo

class AbsorcionConstanteStrategy(EstrategiaAbsorcion[Cultivo]):
    """
    Estrategia concreta: Absorción constante de agua.
    Aplica una absorción fija, típica de hortalizas o árboles jóvenes (US-008).
    """
    
    def absorber_agua(self, cultivo: Cultivo):
        """Implementa la absorción constante (ej: 5 litros por riego)."""
        CANTIDAD_ABSORBIDA = 5
        cultivo.set_agua(cultivo.get_agua() + CANTIDAD_ABSORBIDA)