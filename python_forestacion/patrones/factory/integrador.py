"""
Archivo integrador generado automaticamente
Directorio: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/patrones/factory
Fecha: 2025-10-22 12:40:53
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/patrones/factory/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: cultivo_factory.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/patrones/factory/cultivo_factory.py
# ================================================================================

from python_forestacion.entidades.cultivos.cultivo import Cultivo
# Importar todos los tipos de cultivos concretos
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
# Importar las estrategias para inyectarlas (US-008)
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from typing import Type

class CultivoFactory:
    """Patrón Factory Method Estático para la creación de Cultivos (US-005, US-006)."""
    
    @staticmethod
    def crear_cultivo(tipo_cultivo: str, **kwargs) -> Cultivo:
        """
        Crea una instancia del Cultivo y le inyecta la Estrategia de Absorción (US-008).
        """
        tipo_cultivo = tipo_cultivo.lower()
        cultivo_map: dict[str, Type[Cultivo]] = {
            "pino": Pino,
            "olivo": Olivo,
            "lechuga": Lechuga,
            "zanahoria": Zanahoria,
        }
        
        cultivo_class = cultivo_map.get(tipo_cultivo)
        if not cultivo_class:
            raise ValueError(f"Tipo de cultivo '{tipo_cultivo}' no soportado por el Factory.")

        # Crear la instancia del cultivo
        cultivo_instance = cultivo_class(**kwargs)
        
        # Inyectar la estrategia basada en el tipo (Patrón Strategy US-008)
        estrategia = AbsorcionConstanteStrategy() # Default
        if tipo_cultivo in ["olivo", "pino"]:
            estrategia = AbsorcionSeasonalStrategy()
        
        cultivo_instance.set_estrategia(estrategia)
        
        return cultivo_instance

