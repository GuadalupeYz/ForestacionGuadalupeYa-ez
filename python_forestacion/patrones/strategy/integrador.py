"""
Archivo integrador generado automaticamente
Directorio: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/patrones/strategy
Fecha: 2025-10-22 10:21:44
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/patrones/strategy/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: absorcion_agua_strategy.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/patrones/strategy/absorcion_agua_strategy.py
# ================================================================================

from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Union

# Definimos TypeVar T_Contexto para que la estrategia sepa con qué trabajar (Cultivo en este caso)
T_Contexto = TypeVar('T_Contexto')

class EstrategiaAbsorcion(Generic[T_Contexto], ABC):
    """
    Interfaz/Clase Abstracta para el Patrón Strategy (US-008).
    Define la operación principal para la absorción de agua.
    """
    
    @abstractmethod
    def absorber_agua(self, contexto: T_Contexto):
        """
        Implementa el algoritmo de absorción.
        En este contexto, contexto es una instancia de Cultivo.
        """
        pass

