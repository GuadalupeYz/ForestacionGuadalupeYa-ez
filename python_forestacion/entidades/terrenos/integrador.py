"""
Archivo integrador generado automaticamente
Directorio: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/entidades/terrenos
Fecha: 2025-10-22 12:40:53
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/entidades/terrenos/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: plantacion.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/entidades/terrenos/plantacion.py
# ================================================================================

# python_forestacion/entidades/terrenos/plantacion.py

from python_forestacion.entidades.cultivos.cultivo import Cultivo # Asumo que Cultivo está correctamente definido
from python_forestacion.constantes import AGUA_DEFAULT_PLANTACION
from .tierra import Tierra # Asumo que Tierra se importa de forma relativa
from typing import List, Any, Optional
# No se necesita importar CultivoServiceRegistry aquí, solo en los servicios

class Plantacion:
    """Entidad que representa una plantación agrícola."""
    
    # CRÍTICO: La firma debe coincidir con la llamada de TierraService y agregar 'agua_inicial'
    def __init__(self, 
                 id_padron: int, 
                 superficie: float, 
                 domicilio: str, 
                 nombre_plantacion: str,
                 agua_inicial: float # <-- ARGUMENTO FALTANTE AHORA AGREGADO
                 ):
        
        # 1. Inicializar atributos
        self._id: int = id_padron
        self._nombre: str = nombre_plantacion
        self._superficie: float = superficie
        self._cultivos: List[Any] = [] 
        
        # 2. Inicializar Tierra (usa los argumentos que ya pasamos)
        # Nota: La Plantacion puede contener una referencia a Tierra, pero la Tierra
        # debería crearse con la Plantacion dentro del servicio. Aquí, la creamos 
        # directamente si el servicio así lo dicta.
        # CRÍTICO: El constructor de Tierra solo debe aceptar id_padron, superficie, domicilio.
        self._tierra: Tierra = Tierra(id_padron, superficie, domicilio) 
        
        # 3. Inicializar Agua
        self._agua_disponible: float = agua_inicial # Usamos el valor pasado

    # --- Getters ---
    
    def get_tierra(self) -> Tierra: 
        return self._tierra
        
    def get_cultivos(self) -> List[Any]: 
        return self._cultivos
        
    def add_cultivo(self, cultivo: Any): 
        self._cultivos.append(cultivo)
        
    def get_nombre(self) -> str:
        return self._nombre
        
    def get_agua_disponible(self) -> float: 
        return self._agua_disponible
        
    def get_superficie(self) -> float:
        return self._superficie
        
    # --- Setters/Mutators ---
        
    def set_agua_disponible(self, agua: float): 
        self._agua_disponible = agua
        
    def set_tierra(self, tierra: Tierra):
        self._tierra = tierra

    # --- Métodos de Negocio ---
    
    def get_superficie_maxima(self) -> float:
        """Retorna la superficie máxima total de la Plantación (la de la Tierra)."""
        # Debe devolver su propia superficie, que es la misma que la de la tierra.
        return self._superficie 

    def get_superficie_ocupada(self) -> float:
        """Calcula y retorna la suma de las superficies de todos los cultivos."""
        # Asumo que cada cultivo tiene un método get_superficie()
        return sum(cultivo.get_superficie() for cultivo in self._cultivos)

    def get_superficie_disponible(self) -> float:
        """Calcula y retorna la superficie libre."""
        return self.get_superficie_maxima() - self.get_superficie_ocupada()
        
    def get_id(self) -> int: 
        return self._id
        
    # Asumo que necesitas este método para asignarle trabajadores en main.py
    def get_trabajadores(self) -> List[Any]:
        # Si tienes trabajadores en Plantacion, debes inicializarlos y retornarlos.
        # Si no, asumo que los guardas en la Tierra o en un atributo.
        # Por ahora, devuelvo una lista vacía o asumo un atributo _trabajadores:
        if not hasattr(self, '_trabajadores'):
            self._trabajadores = []
        return self._trabajadores
        
    def set_trabajadores(self, trabajadores: List[Any]):
        self._trabajadores = trabajadores

# ================================================================================
# ARCHIVO 3/4: registro_forestal.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/entidades/terrenos/registro_forestal.py
# ================================================================================

# Archivo: python_forestacion/entidades/terrenos/registro_forestal.py
# ESTE ARCHIVO DEBE CONTENER LA CLASE ENTIDAD 'RegistroForestal'

from datetime import date
from typing import List, Optional
from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion

class RegistroForestal:
    """
    Representa el registro formal y catastral de una finca y su plantación.
    (US-003)
    """
    def __init__(self, id_padron: int, tierra: Tierra, plantacion: Plantacion, propietario: str, avaluo: float, fecha_registro: date = None):
        self._id_padron = id_padron
        self._tierra = tierra # Composición: Una Tierra
        self._plantacion = plantacion # Composición: Una Plantacion
        self._propietario = propietario
        self._avaluo = avaluo
        self._fecha_registro = fecha_registro if fecha_registro is not None else date.today()

    # --- Getters (US-003) ---
    def get_id_padron(self) -> int:
        return self._id_padron

    def get_tierra(self) -> Tierra:
        return self._tierra

    def get_plantacion(self) -> Plantacion:
        return self._plantacion

    def get_propietario(self) -> str:
        return self._propietario

    def get_avaluo(self) -> float:
        return self._avaluo

    def get_fecha_registro(self) -> date:
        return self._fecha_registro

    def __str__(self):
        return (f"Registro Forestal #{self._id_padron} - Propietario: {self._propietario}\n"
                f"  Plantación: {self._plantacion.get_nombre()} ({len(self._plantacion.get_cultivos())} cultivos)\n"
                f"  Superficie Total: {self._tierra.get_superficie():.2f} m²")

# ================================================================================
# ARCHIVO 4/4: tierra.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/entidades/terrenos/tierra.py
# ================================================================================

from typing import Optional, TYPE_CHECKING
# Usamos TYPE_CHECKING y comillas para romper dependencias circulares y evitar warnings
if TYPE_CHECKING:
    from .plantacion import Plantacion

class Tierra:
    """Entidad Tierra (Terreno) (US-001)."""
    
    def __init__(self, id_padron: int, superficie: float, domicilio: str):
        self._id_padron = id_padron
        self._superficie = superficie
        self._domicilio = domicilio
        self._finca: Optional['Plantacion'] = None # Usamos comillas

    def get_superficie(self) -> float: 
        return self._superficie

    def get_domicilio(self):  # <- asegurate que se llama así
        return self._domicilio

    def set_finca(self, plantacion: 'Plantacion'): self._finca = plantacion # Usamos comillas
    def get_finca(self) -> Optional['Plantacion']: return self._finca # Usamos comillas
    # ... (Otros getters necesarios)

    def get_id_padron(self):
     return self._id_padron
    

