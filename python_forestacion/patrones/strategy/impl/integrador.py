"""
Archivo integrador generado automaticamente
Directorio: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/patrones/strategy/impl
Fecha: 2025-10-22 10:21:44
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/patrones/strategy/impl/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: absorcion_constante_strategy.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/patrones/strategy/impl/absorcion_constante_strategy.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/3: absorcion_seasonal_strategy.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/patrones/strategy/impl/absorcion_seasonal_strategy.py
# ================================================================================

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

