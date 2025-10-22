"""
Archivo integrador generado automaticamente
Directorio: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/entidades/cultivos
Fecha: 2025-10-22 10:21:44
Total de archivos integrados: 9
"""

# ================================================================================
# ARCHIVO 1/9:  __init__.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/entidades/cultivos/ __init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/9: arbol.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/entidades/cultivos/arbol.py
# ================================================================================

from .cultivo import Cultivo

class Arbol(Cultivo):
    """Clase base para todos los tipos de árboles."""
    def __init__(self, nombre: str = None, **kwargs):  # ← Cambiar _init_ por __init__
        self._nombre = nombre
        self._altura_metros = kwargs.pop('altura_metros', 0.0)
        self._edad_anios = kwargs.pop('edad_anios', 0)
        nombre_cultivo = kwargs.pop('nombre', 'Árbol Base')
        superficie_cultivo = kwargs.pop('superficie', 0.0)
        agua_cultivo = kwargs.pop('agua_inicial', 0.0)
        super().__init__(  # ← Cambiar _init_ por __init__
            nombre=nombre_cultivo,
            superficie=superficie_cultivo,
            agua_inicial=agua_cultivo,
            **kwargs
        )
    
    def get_edad_anios(self) -> int:
        return self._edad_anios
    
    def get_altura(self) -> float:
        return self._altura_metros
    
    def get_edad(self) -> int:
        """Método de compatibilidad para evitar errores en Olivo.__str__"""
        return self._edad_anios

# ================================================================================
# ARCHIVO 3/9: cultivo.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/entidades/cultivos/cultivo.py
# ================================================================================

# python_forestacion/entidades/cultivos/cultivo.py

from abc import ABC, abstractmethod
from typing import Optional, TYPE_CHECKING, Any 

if TYPE_CHECKING:
    from python_forestacion.patrones.strategy.absorcion_agua_strategy import EstrategiaAbsorcion

class Cultivo(ABC):
    """Clase base abstracta para todos los cultivos."""
    
    # CRÍTICO: **kwargs debe ser el último argumento.
    def __init__(self, nombre: str, superficie: float, agua_inicial: float, **kwargs):
        self._nombre = nombre
        self._superficie = superficie
        self._agua = agua_inicial 
        self._id: Optional[int] = None
        self._estrategia: Optional['EstrategiaAbsorcion'] = None
        self._esta_plantado = False 
        self._fase_crecimiento = 0

        # IMPORTANTE: Aquí se descartan los kwargs sobrantes (como 'variedad').
        # Si NO consumes el 'variedad' en Olivo ni en Arbol, aquí se descartaría finalmente.
        
        # Consumir (o simplemente ignorar) cualquier argumento restante en kwargs.
        # Si Cultivo hereda de ABC, su padre es 'object'. 
        # object.__init__() NO acepta **kwargs.
        # Por lo tanto, cualquier cosa que quede en kwargs DEBE ser vaciada aquí.
        if kwargs:
            # print(f"[DEBUG]: Argumentos sobrantes descartados en Cultivo: {kwargs.keys()}") # Opcional para depuración
            kwargs.clear() # ¡Esta es la clave! Vaciar el diccionario para que no cause TypeError.

    # --- Getters/Setters esenciales:
    def get_edad_anios(self) -> int:
        # ESTE MÉTODO DEBE ESTAR EN ARBOL, NO EN CULTIVO.
        # Si está aquí, causará confusión.
        # Para compatibilidad temporal, devuelve un valor por defecto.
        # Pero a la larga, debe eliminarse de Cultivo.
        return getattr(self, '_edad_anios', 0) 
    
    def get_nombre(self) -> str:
        return self._nombre

    def get_agua(self) -> float:
        return self._agua
    
    def set_agua(self, cantidad: float):
        self._agua = cantidad
        
    def get_superficie(self) -> float: 
        return self._superficie
        
    def set_id(self, id_val: int): 
        self._id = id_val
        
    def get_id(self) -> Optional[int]: 
        return self._id
    
    # Métodos de Estrategia (US-008):
    def set_estrategia(self, estrategia: 'EstrategiaAbsorcion'): 
        self._estrategia = estrategia
        
    def get_estrategia(self) -> 'EstrategiaAbsorcion':
        if not self._estrategia:
            raise AttributeError(f"El cultivo {self._nombre} no tiene estrategia de absorción asignada.")
        return self._estrategia

    # Método abstracto:
    @abstractmethod
    def __str__(self) -> str:
        pass

# ================================================================================
# ARCHIVO 4/9: hortaliza.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/entidades/cultivos/hortaliza.py
# ================================================================================

# Contenido esperado en hortaliza.py

from .cultivo import Cultivo

class Hortaliza(Cultivo):
    """Clase base para todos los tipos de hortalizas."""
    def __init__(self, **kwargs):
        # Simplemente llama al constructor de la clase padre (Cultivo) 
        # y le pasa TODOS los argumentos restantes.
        super().__init__(**kwargs)


# ================================================================================
# ARCHIVO 5/9: lechuga.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/entidades/cultivos/lechuga.py
# ================================================================================

from .hortaliza import Hortaliza
from python_forestacion.constantes import SUPERFICIE_LECHUGA, AGUA_INICIAL_LECHUGA
# Contenido CORREGIDO y CONSISTENTE en lechuga.py

class Lechuga(Hortaliza):
    def __init__(self, **kwargs): 
        peso = kwargs.pop('peso', 1.0)
        variedad = kwargs.pop('variedad', 'Desconocida')
        super().__init__(
            nombre="Lechuga",
            agua_inicial=AGUA_INICIAL_LECHUGA,
            superficie=SUPERFICIE_LECHUGA,
            **kwargs
        )
        self._peso_unidad = peso
        self._variedad = variedad

    # 3. Getter para el peso (usado en la cosecha y visualización)
    def get_peso(self) -> float:
        return self._peso_unidad
        
    # 4. Getter para la variedad (usado en el Service)
    def get_variedad(self) -> str:
        return self._variedad
        
    def __str__(self) -> str:
        return f"Lechuga ({self._variedad} - {self._peso_unidad:.2f}kg)"

    # Contenido CORREGIDO en lechuga.py (Asumo que hereda de Hortaliza)



# ================================================================================
# ARCHIVO 6/9: olivo.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/entidades/cultivos/olivo.py
# ================================================================================

# python_forestacion/entidades/cultivos/olivo.py
from .arbol import Arbol
from .tipo_aceituna import TipoAceituna 
# ELIMINAR CUALQUIER OTRA IMPORTACIÓN DE TIPOACEITUNA
from python_forestacion.constantes import SUPERFICIE_OLIVO, AGUA_INICIAL_OLIVO

class Olivo(Arbol):
    
    def __init__(self, **kwargs):
        
        # 1. Extraer y preparar el Enum ANTES de llamar a super()
        variedad_str = kwargs.pop('variedad', kwargs.pop('tipo_aceituna', 'MANZANILLA'))
        
        try:
             # Aquí variedad_enum es temporal
             variedad_enum = TipoAceituna[variedad_str.upper()]
        except KeyError:
             variedad_enum = TipoAceituna.MANZANILLA
        
        # 2. Asignar el atributo específico del Olivo
        # ¡IMPORTANTE! Lo ponemos aquí para que el objeto se "complete" antes del super si es posible.
        self._tipo_aceituna = variedad_enum 

        # 3. Llamar a la clase padre (Arbol)
        super().__init__(
            nombre="Olivo",
            agua_inicial=kwargs.pop('agua_inicial', AGUA_INICIAL_OLIVO),
            superficie=kwargs.pop('superficie', SUPERFICIE_OLIVO),
            **kwargs 
        )

    # 4. Implementación CRÍTICA del método abstracto
    # Asegúrate de que no tenga @abstractmethod y tenga 4 espacios de indentación
    def __str__(self) -> str:
        return f"Olivo (Tipo Aceituna: {self._tipo_aceituna.value}, Edad: {self.get_edad_anios()} años)"

    # --- Getters ---

    def get_variedad(self) -> TipoAceituna:
        return self._tipo_aceituna

    def get_tipo_aceituna(self):
        return self._tipo_aceituna


# ================================================================================
# ARCHIVO 7/9: pino.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/entidades/cultivos/pino.py
# ================================================================================

from .arbol import Arbol
from python_forestacion.constantes import SUPERFICIE_PINO, AGUA_INICIAL_PINO

class Pino(Arbol):
    """Cultivo concreto: Pino (US-005)."""
    def __init__(self, variedad: str = None, altura_metros: float = 0.0, edad_anios: int = 0):  # ← Cambiar _init_ por __init__
        super().__init__(  # ← Cambiar _init_ por __init__
            nombre="Pino",
            altura_metros=altura_metros,
            edad_anios=edad_anios,
            superficie=SUPERFICIE_PINO,
            agua_inicial=AGUA_INICIAL_PINO
        )
        self._variedad = variedad  # atributo específico de Pino
    
    def __str__(self) -> str:  # ← Cambiar _str_ por __str__
        return f"Pino (Edad: {self.get_edad_anios()} años, Altura: {self.get_altura()} m, Variedad: {self._variedad})"
    
    def get_variedad(self) -> str:
        return self._variedad

# ================================================================================
# ARCHIVO 8/9: tipo_aceituna.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/entidades/cultivos/tipo_aceituna.py
# ================================================================================

from enum import Enum

class TipoAceituna(Enum):
    """Enum para los tipos de aceituna del Olivo."""
    MANZANILLA = "Manzanilla"
    ARBEQUINA = "Arbequina"
    PICUAL = "Picual"
    def __str__ (self):
        return self.value

# ================================================================================
# ARCHIVO 9/9: zanahoria.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/entidades/cultivos/zanahoria.py
# ================================================================================

from .hortaliza import Hortaliza
from python_forestacion.constantes import SUPERFICIE_ZANAHORIA, AGUA_INICIAL_ZANAHORIA

class Zanahoria(Hortaliza):
    def __init__(self, **kwargs):
        # 1. Extraer los parámetros específicos con valores por defecto
        self._es_baby_carrot = kwargs.pop('es_baby_carrot', False)
        self._longitud = kwargs.pop('longitud', 0.15)  # valor por defecto razonable

        # 2. Llamar a la clase padre (Hortaliza)
        super().__init__(
            nombre="Zanahoria",
            agua_inicial=AGUA_INICIAL_ZANAHORIA,
            superficie=SUPERFICIE_ZANAHORIA,
            **kwargs
        )

    def es_baby_carrot(self) -> bool:
        return self._es_baby_carrot

    def get_longitud(self) -> float:
        return self._longitud

    def __str__(self) -> str:
        tipo = "Baby Carrot" if self._es_baby_carrot else "Zanahoria común"
        return f"{tipo} (Longitud: {self._longitud:.2f}m)"


