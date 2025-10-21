from ..absorcion_agua_strategy import EstrategiaAbsorcion 
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.constantes import ABSORCION_VERANO, ABSORCION_INVIERNO
from datetime import date

class AbsorcionSeasonalStrategy(EstrategiaAbsorcion[Cultivo]):
    """
    Estrategia concreta: Absorción estacional de agua (US-008).
    Aplica una absorción que varía según el mes o estación.
    """
    
    def absorber_agua(self, cultivo: Cultivo):
        """Implementa la absorción variable basada en la estación (simulada por mes)."""
        mes_actual = date.today().month
        
        CANTIDAD_ABSORBIDA = 10 # Base para todos los riegos
        
        # Argentina (Hemisferio Sur): Verano (Dic, Ene, Feb), Invierno (Jun, Jul, Ago)
        if mes_actual in [12, 1, 2]: 
            CANTIDAD_ABSORBIDA += ABSORCION_VERANO
        elif mes_actual in [6, 7, 8]:
            CANTIDAD_ABSORBIDA += ABSORCION_INVIERNO
        
        cultivo.set_agua(cultivo.get_agua() + CANTIDAD_ABSORBIDA)