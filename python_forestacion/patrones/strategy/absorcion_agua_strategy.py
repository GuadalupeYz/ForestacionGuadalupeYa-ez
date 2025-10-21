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