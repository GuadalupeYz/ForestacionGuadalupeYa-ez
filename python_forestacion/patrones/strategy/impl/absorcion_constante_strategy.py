# Contenido CORREGIDO de python_forestacion/patrones/strategy/impl/absorcion_constante_strategy.py

from ..absorcion_agua_strategy import EstrategiaAbsorcion 
from python_forestacion.entidades.cultivos.cultivo import Cultivo

class AbsorcionConstanteStrategy(EstrategiaAbsorcion[Cultivo]):
    
    # CRÍTICO: Añadir un valor por defecto (ej. 1.0) para que el argumento sea opcional.
    def __init__(self, cantidad_constante: float = 1.0): 
        self._cantidad_constante = cantidad_constante

    def absorber_agua(self, cultivo: Cultivo):
        """Implementa la absorción constante, usando el valor del constructor."""
        # Retornamos la cantidad para que CultivoService.regar la aplique.
        return self._cantidad_constante
