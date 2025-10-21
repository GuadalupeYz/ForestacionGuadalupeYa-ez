from abc import ABC, abstractmethod
from typing import Any
# Asumo que Cultivo y Plantacion ya están definidos y son accesibles.
# from python_forestacion.entidades.cultivos.cultivo import Cultivo
# from python_forestacion.entidades.terrenos.plantacion import Plantacion

class CultivoService(ABC):
    """
    Clase base abstracta (interfaz) para todos los servicios de cultivos concretos.
    Define los métodos esenciales que debe soportar un servicio de cultivo
    para ser utilizado por el CultivoServiceRegistry (US-009).
    """

    @abstractmethod
    def mostrar_info(self, cultivo: Any):
        """
        Muestra la información específica y relevante del tipo de cultivo.
        Debe ser implementado por clases concretas como PinoService o OlivoService.
        """
        pass

    # Puedes agregar otros métodos abstractos necesarios aquí, como:
    # @abstractmethod
    # def realizar_mantenimiento(self, cultivo: Any):
    #     pass