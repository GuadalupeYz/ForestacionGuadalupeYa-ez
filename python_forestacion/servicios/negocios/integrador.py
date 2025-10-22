"""
Archivo integrador generado automaticamente
Directorio: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/servicios/negocios
Fecha: 2025-10-22 10:21:44
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/servicios/negocios/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: fincas_service.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/servicios/negocios/fincas_service.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/3: paquete.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/servicios/negocios/paquete.py
# ================================================================================

from typing import Generic, TypeVar, Optional
from datetime import datetime

# T es el tipo de datos que encapsula el paquete (Cultivo o Plantacion)
T = TypeVar('T', bound=object) 
# No se necesitan imports de Cultivo o Plantacion si solo se usa 'T'

class Paquete(Generic[T]):
    """
    Entidad Paquete (DTO) que encapsula un Cultivo o una Plantacion (US-018).
    Se ubica aquí siguiendo la estructura provista.
    """
    
    def __init__(self, elemento: T, etiqueta: Optional[str] = None):
        self._elemento: T = elemento
        self._etiqueta = etiqueta 
        self._fecha_creacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_elemento(self) -> T:
        return self._elemento
        
    def __str__(self) -> str:
        # Usa elemento.__class__.__name__ para obtener el nombre de la clase
        return (f"Paquete [{self._elemento.__class__.__name__}] (Fecha: {self._fecha_creacion}, "
                f"Etiqueta: {self._etiqueta if self._etiqueta else 'N/A'})")

