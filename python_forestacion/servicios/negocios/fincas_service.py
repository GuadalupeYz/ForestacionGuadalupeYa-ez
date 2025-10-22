# Asumo que estas importaciones son necesarias para el cuerpo de la clase
from ..terrenos.plantacion_service import PlantacionService
from ..terrenos.registro_forestal_service import RegistroForestalService 
from ..cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from .paquete import Paquete
from typing import Any, Dict

class FincasService:
    """
    Servicio de alto nivel que coordina operaciones de negocio (US-001, US-019).
    """

    # MODIFICACIÓN CLAVE AQUÍ: Aceptar registro_service
    def __init__(self, registro_service: RegistroForestalService):
        # Guardar el servicio de persistencia
        self._registro_service = registro_service 
        # Inicializar servicios internos necesarios
        self._plantacion_service = PlantacionService()
        self._cultivo_registry = CultivoServiceRegistry.get_instance()
        self._fincas = [] 
        
    def add_finca(self, finca: Any):
     self._fincas.append(finca)

    def crear_plantacion(self, id_padron: int, superficie: float, domicilio: str, nombre_plantacion: str) -> Plantacion:
        """Crea una Tierra y una Plantacion asociadas (US-001)."""
        nueva_tierra = Tierra(id_padron, superficie, domicilio)
        nueva_plantacion = Plantacion(nombre_plantacion, nueva_tierra)
        return nueva_plantacion
        
    def regar_y_mostrar_info(self, plantacion: Plantacion):
        """Muestra la info de cada cultivo y realiza un riego forzado."""
        print(f"-> Regando la plantación {plantacion._nombre}...")
        self._plantacion_service.regar(plantacion)
        print("-> Información de cultivos después del riego:")
        for cultivo in plantacion.get_cultivos():
            self._cultivo_registry.mostrar_datos(cultivo)

    # Puedes agregar aquí el resto de los métodos (crear_paquetes, etc.)
    def crear_paquetes(self, cultivos: list, nombre_lote: str):
        # Simula la lógica de empaquetado (US-019)
        print(f"[PAQUETES]: Creado lote '{nombre_lote}' con {len(cultivos)} unidades.")


    def cosechar_y_empaquetar(self, plantacion):
        """Simula la cosecha y creación de paquetes para todos los cultivos"""
        print(f"-> Cosechando todos los cultivos de '{plantacion._nombre}'...")
        cultivos = plantacion.get_cultivos()
        for cultivo in cultivos:
            print(f"   Cosechando: {cultivo}")
        self.crear_paquetes(cultivos, f"Lote_{plantacion._nombre}")
        cultivos_cosechados = []
        for finca in self._fincas:
          plantacion = finca.get_plantacion()
        for cultivo in plantacion.get_cultivos():
            if isinstance(cultivo):
                cultivos_cosechados.append(cultivo)

        paquetes = [Paquete(cultivo) for cultivo in cultivos_cosechados]
        return paquetes
