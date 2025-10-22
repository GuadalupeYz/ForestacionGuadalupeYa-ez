"""
INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO
============================================================================
Directorio raiz: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion
Fecha de generacion: 2025-10-22 10:21:44
Total de archivos integrados: 68
Total de directorios procesados: 21
============================================================================
"""

# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================
# DIRECTORIO: ..python buscar_paquete.py integrar python_forestacion
#   1. main.py
#
# DIRECTORIO: .
#   2. __init__.py
#   3. constantes.py
#
# DIRECTORIO: entidades
#   4. __init__.py
#
# DIRECTORIO: entidades/cultivos
#   5.  __init__.py
#   6. arbol.py
#   7. cultivo.py
#   8. hortaliza.py
#   9. lechuga.py
#   10. olivo.py
#   11. pino.py
#   12. tipo_aceituna.py
#   13. zanahoria.py
#
# DIRECTORIO: entidades/personal
#   14. __init__.py
#   15. apto_medico.py
#   16. herramienta.py
#   17. tarea.py
#   18. trabajador.py
#
# DIRECTORIO: entidades/terrenos
#   19. __init__.py
#   20. plantacion.py
#   21. registro_forestal.py
#   22. tierra.py
#
# DIRECTORIO: excepciones
#   23. __init__.py
#   24. agua_agotada_exception.py
#   25. forestacion_exception.py
#   26. mensajes_exception.py
#   27. persistencia_exception.py
#   28. superficie_insuficiente_exception.py
#
# DIRECTORIO: patrones
#   29. __init__.py
#
# DIRECTORIO: patrones/factory
#   30. __init__.py
#   31. cultivo_factory.py
#
# DIRECTORIO: patrones/observer
#   32. __init__.py
#   33. observable.py
#   34. observer.py
#
# DIRECTORIO: patrones/observer/eventos
#   35. __init__.py
#   36. evento_plantacion.py
#   37. evento_sensor.py
#
# DIRECTORIO: patrones/singleton
#   38. __init__.py
#   39. singleton.py
#
# DIRECTORIO: patrones/strategy
#   40. __init__.py
#   41. absorcion_agua_strategy.py
#
# DIRECTORIO: patrones/strategy/impl
#   42. __init__.py
#   43. absorcion_constante_strategy.py
#   44. absorcion_seasonal_strategy.py
#
# DIRECTORIO: riego
#   45. __init__.py
#
# DIRECTORIO: riego/control
#   46. __init__.py
#   47. control_riego_task.py
#
# DIRECTORIO: riego/sensores
#   48. __init__.py
#   49. humedad_reader_task.py
#   50. temperatura_reader_task.py
#
# DIRECTORIO: servicios
#   51. __init__.py
#
# DIRECTORIO: servicios/cultivos
#   52. __init__.py
#   53. arbol_service.py
#   54. cultivo_service.py
#   55. cultivo_service_registry.py
#   56. lechuga_service.py
#   57. olivo_service.py
#   58. pino_service.py
#   59. zanahoria_service.py
#
# DIRECTORIO: servicios/negocios
#   60. __init__.py
#   61. fincas_service.py
#   62. paquete.py
#
# DIRECTORIO: servicios/personal
#   63. __init__.py
#   64. trabajador_service.py
#
# DIRECTORIO: servicios/terrenos
#   65. __init__.py
#   66. plantacion_service.py
#   67. registro_forestal_service.py
#   68. tierra_service.py
#



################################################################################
# DIRECTORIO: .
################################################################################

# ==============================================================================
# ARCHIVO 1/68: main.py
# Directorio: ..
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/main.py
# ==============================================================================

# ==============================================================================
# ARCHIVO 2/68: __init__.py
# Directorio: .
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 3/68: constantes.py
# Directorio: .
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/constantes.py
# ==============================================================================

# --- Constantes para Persistencia ---
DIRECTORIO_DATA = "data"
EXTENSION_DATA = ".dat"

# --- Constantes para Concurrencia (threads) ---
THREAD_JOIN_TIMEOUT = 1.0 # Tiempo en segundos para esperar que los hilos terminen (1.0 segundo es un valor típico)
SENSOR_LECTURA_INTERVALO = 2 # Segundos entre lecturas de sensores
CONTROL_RIEGO_INTERVALO = 3 # Segundos entre chequeos del controlador de riego

# --- Constantes para Superficie (m²) ---
SUPERFICIE_PINO = 2.0
SUPERFICIE_OLIVO = 3.0
SUPERFICIE_LECHUGA = 0.1
SUPERFICIE_ZANAHORIA = 0.05

# --- Constantes para Agua Inicial (Litros) ---
AGUA_INICIAL_PINO = 100
AGUA_INICIAL_OLIVO = 80
AGUA_INICIAL_LECHUGA = 10
AGUA_INICIAL_ZANAHORIA = 5

# --- Constantes de Riego y Plantación ---
AGUA_DEFAULT_PLANTACION = 5000
AGUA_MINIMA_RIEGOS = 1000 # Mínimo de agua para iniciar el riego automático

# --- Constantes de Simulación Concurrente ---
TIEMPO_LECTURA_SENSOR = 2.0 # Segundos
UMBRAL_TEMPERATURA = 25.0 # Grados Celsius
UMBRAL_HUMEDAD = 40.0 # Porcentaje

# --- Constantes de Absorción Estacional (NUEVAS LÍNEAS) ---
ABSORCION_VERANO = 20 # Litros extra de agua absorbida en verano (factor alto)
ABSORCION_INVIERNO = 5 # Litros extra de agua absorbida en invierno (factor bajo)

# ... (Todo el contenido anterior de constantes.py) ...

# Archivo: python_forestacion/constantes.py (o donde esté TipoOperacion)
from enum import Enum

class TipoOperacion(Enum):
    """Tipos de operaciones para registrar y centralizar mensajes de error."""
    PLANTACION = "PLANTACIÓN"
    RIEGO = "RIEGO"
    COSECHA = "COSECHA"
    PERSISTENCIA = "PERSISTENCIA"
    CONCURRENCIA = "CONCURRENCIA"
    # --- ¡AGREGA O VERIFICA ESTO! ---
    CARGA = "CARGA"      # Necesario para la función leer_registro o from_deserialization_exception
    GUARDADO = "GUARDADO" # Si usas GUARDADO en persistir()
    LECTURA = "LECTURA"   # Si usas LECTURA en from_deserialization_exception
    # ---------------------------------


################################################################################
# DIRECTORIO: entidades
################################################################################

# ==============================================================================
# ARCHIVO 4/68: __init__.py
# Directorio: entidades
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/entidades/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: entidades/cultivos
################################################################################

# ==============================================================================
# ARCHIVO 5/68:  __init__.py
# Directorio: entidades/cultivos
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/entidades/cultivos/ __init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 6/68: arbol.py
# Directorio: entidades/cultivos
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/entidades/cultivos/arbol.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 7/68: cultivo.py
# Directorio: entidades/cultivos
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/entidades/cultivos/cultivo.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 8/68: hortaliza.py
# Directorio: entidades/cultivos
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/entidades/cultivos/hortaliza.py
# ==============================================================================

# Contenido esperado en hortaliza.py

from .cultivo import Cultivo

class Hortaliza(Cultivo):
    """Clase base para todos los tipos de hortalizas."""
    def __init__(self, **kwargs):
        # Simplemente llama al constructor de la clase padre (Cultivo) 
        # y le pasa TODOS los argumentos restantes.
        super().__init__(**kwargs)


# ==============================================================================
# ARCHIVO 9/68: lechuga.py
# Directorio: entidades/cultivos
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/entidades/cultivos/lechuga.py
# ==============================================================================

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



# ==============================================================================
# ARCHIVO 10/68: olivo.py
# Directorio: entidades/cultivos
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/entidades/cultivos/olivo.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 11/68: pino.py
# Directorio: entidades/cultivos
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/entidades/cultivos/pino.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 12/68: tipo_aceituna.py
# Directorio: entidades/cultivos
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/entidades/cultivos/tipo_aceituna.py
# ==============================================================================

from enum import Enum

class TipoAceituna(Enum):
    """Enum para los tipos de aceituna del Olivo."""
    MANZANILLA = "Manzanilla"
    ARBEQUINA = "Arbequina"
    PICUAL = "Picual"
    def __str__ (self):
        return self.value

# ==============================================================================
# ARCHIVO 13/68: zanahoria.py
# Directorio: entidades/cultivos
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/entidades/cultivos/zanahoria.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: entidades/personal
################################################################################

# ==============================================================================
# ARCHIVO 14/68: __init__.py
# Directorio: entidades/personal
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/entidades/personal/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 15/68: apto_medico.py
# Directorio: entidades/personal
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/entidades/personal/apto_medico.py
# ==============================================================================

# Archivo: python_forestacion/entidades/personal/apto_medico.py
from datetime import date
from typing import Optional

class AptoMedico:
    """Representa el certificado de aptitud de un trabajador."""
    
    def __init__(self, apto: bool, fecha_emision: date, observaciones: Optional[str] = None):
        self._apto = apto
        self._fecha_emision = fecha_emision
        self._observaciones = observaciones or "Sin observaciones"

    def esta_apto(self) -> bool:
        """Retorna True si el trabajador está certificado como apto."""
        # NOTA: En un sistema real se chequearía la fecha de vencimiento (fecha_emision + X años).
        return self._apto

    def get_fecha_emision(self) -> date:
        return self._fecha_emision

    def get_observaciones(self) -> str:
        return self._observaciones

    def __str__(self):
        estado = "APTO" if self._apto else "NO APTO"
        return f"Certificado: {estado} (Emitido: {self._fecha_emision})"

# ==============================================================================
# ARCHIVO 16/68: herramienta.py
# Directorio: entidades/personal
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/entidades/personal/herramienta.py
# ==============================================================================

class Herramienta:
    """Representa una herramienta de trabajo con ID único y certificación H&S."""
    
    _next_id = 1 # Contador para asignar IDs únicos

    def __init__(self, nombre: str, descripcion: str, certificacion_hs: bool, operativa: bool = True):
        # Asignación de ID único
        self._id = Herramienta._next_id
        Herramienta._next_id += 1
        
        self._nombre = nombre
        self._descripcion = descripcion
        self._operativa = operativa
        self._certificacion_hs = certificacion_hs # Requisito del README: Certificación H&S

    def get_id(self) -> int:
        """Obtiene el ID único de la herramienta."""
        return self._id

    def get_nombre(self) -> str:
        return self._nombre

    def esta_operativa(self) -> bool:
        """Verifica si la herramienta está en condiciones de uso."""
        return self._operativa

    def tiene_certificacion_hs(self) -> bool:
        """Verifica si la herramienta posee la certificación de Salud y Seguridad (H&S)."""
        return self._certificacion_hs

    def set_operativa(self, estado: bool):
        """Cambia el estado operativo de la herramienta (ej. por avería)."""
        self._operativa = estado

    def __str__(self):
        estado = "Operativa" if self._operativa else "En Reparación"
        cert = "Certificada H&S" if self._certificacion_hs else "NO Certificada"
        return f"Herramienta #{self._id}: {self._nombre} ({estado}, {cert})"

# ==============================================================================
# ARCHIVO 17/68: tarea.py
# Directorio: entidades/personal
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/entidades/personal/tarea.py
# ==============================================================================

from datetime import date
from enum import Enum
from typing import Optional

class EstadoTarea(Enum):
    PENDIENTE = "Pendiente"
    COMPLETADA = "Completada"

class Tarea:
    """Representa una labor asignada con estado y fecha programada, usando solo PENDIENTE/COMPLETADA."""
    
    _next_id = 1 # Para asignacion de ID unico (para orden descendente de ejecucion)

    def __init__(self, nombre: str, descripcion: str, fecha_programada: date, herramienta_requerida: Optional[str] = None, estado: EstadoTarea = EstadoTarea.PENDIENTE):
        self._id = Tarea._next_id
        Tarea._next_id += 1
        self._nombre = nombre
        self._descripcion = descripcion
        self._fecha_programada = fecha_programada
        self._estado = estado
        self._herramienta_requerida = herramienta_requerida # Opcional: para enlazar con Herramienta

    def get_id(self) -> int:
        """ID único de la tarea para la ejecución ordenada (descendente por ID)."""
        return self._id

    def get_nombre(self) -> str:
        return self._nombre
    
    def get_estado(self) -> EstadoTarea:
        """Estado de tareas (pendiente/completada)."""
        return self._estado

    def get_fecha_programada(self) -> date:
        return self._fecha_programada

    def marcar_completada(self):
        """Cambia el estado de la tarea a COMPLETADA."""
        self._estado = EstadoTarea.COMPLETADA
        
    def __str__(self):
        return f"Tarea #{self._id}: {self._nombre} (Estado: {self._estado.value}, Fecha: {self._fecha_programada})"

# ==============================================================================
# ARCHIVO 18/68: trabajador.py
# Directorio: entidades/personal
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/entidades/personal/trabajador.py
# ==============================================================================

# Archivo: python_forestacion/entidades/personal/trabajador.py
from typing import List, Optional
from python_forestacion.entidades.personal.tarea import Tarea # Importar Tarea
from python_forestacion.entidades.personal.apto_medico import AptoMedico # Importar AptoMedico
import copy # Necesario para defensive copy (US-014, US-017)

class Trabajador:
    """Representa un trabajador con tareas asignadas y apto médico."""

    def __init__(self, dni: int, nombre: str, tareas: List[Tarea] = None, apto_medico: Optional[AptoMedico] = None):
        self._dni = dni
        self._nombre = nombre
        self._tareas = tareas if tareas is not None else []
        self._apto_medico = apto_medico

    def get_dni(self) -> int:
        return self._dni

    def get_nombre(self) -> str:
        return self._nombre

    def get_tareas_asignadas(self) -> List[Tarea]:
        """Retorna una copia inmutable (defensive copy) de la lista de tareas."""
        return copy.deepcopy(self._tareas)

    def get_apto_medico(self) -> Optional[AptoMedico]:
        return self._apto_medico

    def set_apto_medico(self, apto: AptoMedico):
        """Asigna o actualiza el apto médico."""
        self._apto_medico = apto

    def __str__(self):
        estado_apto = "CON apto" if self._apto_medico and self._apto_medico.esta_apto() else "SIN apto"
        return f"{self._nombre} (DNI: {self._dni}) - {estado_apto}"


################################################################################
# DIRECTORIO: entidades/terrenos
################################################################################

# ==============================================================================
# ARCHIVO 19/68: __init__.py
# Directorio: entidades/terrenos
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/entidades/terrenos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 20/68: plantacion.py
# Directorio: entidades/terrenos
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/entidades/terrenos/plantacion.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 21/68: registro_forestal.py
# Directorio: entidades/terrenos
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/entidades/terrenos/registro_forestal.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 22/68: tierra.py
# Directorio: entidades/terrenos
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/entidades/terrenos/tierra.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: excepciones
################################################################################

# ==============================================================================
# ARCHIVO 23/68: __init__.py
# Directorio: excepciones
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/excepciones/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 24/68: agua_agotada_exception.py
# Directorio: excepciones
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/excepciones/agua_agotada_exception.py
# ==============================================================================

from .forestacion_exception import ForestacionException
from python_forestacion.constantes import TipoOperacion, AGUA_MINIMA_RIEGOS

class AguaAgotadaException(ForestacionException):
    """Excepción lanzada cuando el agua de la plantación es insuficiente para un riego (US-008)."""
    
    def __init__(self, agua_actual: int):
        super().__init__(
            TipoOperacion.RIEGO, 
            "AGUA_AGOTADA", 
            agua_actual=agua_actual, 
            minimo=AGUA_MINIMA_RIEGOS
        )

# ==============================================================================
# ARCHIVO 25/68: forestacion_exception.py
# Directorio: excepciones
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/excepciones/forestacion_exception.py
# ==============================================================================

from .mensajes_exception import MensajeError
from python_forestacion.constantes import TipoOperacion

class ForestacionException(Exception):
    """Clase base para todas las excepciones controladas de la aplicación (US-003)."""

    def __init__(self, tipo: TipoOperacion, codigo: str, **kwargs):
        self._tipo = tipo
        self._codigo = codigo
        self._mensaje_usuario = MensajeError.obtener(tipo, codigo, **kwargs)
        super().__init__(self._mensaje_usuario)

    def get_tipo(self) -> TipoOperacion:
        return self._tipo
    
    def get_user_message(self) -> str:
        """Devuelve el mensaje formateado para el usuario/log."""
        return self._mensaje_usuario

# ==============================================================================
# ARCHIVO 26/68: mensajes_exception.py
# Directorio: excepciones
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/excepciones/mensajes_exception.py
# ==============================================================================

# python_forestacion/excepciones/mensajes_exception.py

from python_forestacion.constantes import TipoOperacion
from typing import Dict, Any
import os # Necesario para usar os.path.basename(nombre_archivo) en la excepción

class MensajeError:
    """Clase estática que contiene los mensajes de error centralizados."""

    MENSAJES: Dict[TipoOperacion, Dict[str, str]] = {
        TipoOperacion.PLANTACION: {
            "SUPERFICIE_INSUF": "Superficie insuficiente. Se requieren {requerida:.2f} m² y solo hay {disponible:.2f} m² disponibles para {tipo}.",
        },
        TipoOperacion.RIEGO: {
            "AGUA_AGOTADA": "Riego fallido. El tanque de la plantación solo tiene {agua_actual} L, que es insuficiente para el riego mínimo ({minimo} L)."
        },
        TipoOperacion.PERSISTENCIA: {
            # Ajustado para que acepte la causa_raiz que PersistenciaException le está enviando
            "CARGA_FALLIDA": "Error al cargar el registro '{nombre_archivo}'. El archivo está corrupto o vacío. Detalle: {causa_raiz}", 
            "GUARDADO_FALLIDO": "Error al guardar el estado del sistema en '{nombre_archivo}'. Causa: {causa_raiz}" 
        }
    }

    @staticmethod
    def obtener(tipo: TipoOperacion, codigo: str, **kwargs) -> str:
        """Obtiene y formatea un mensaje de error según el tipo y código."""
        mensaje_base = MensajeError.MENSAJES.get(tipo, {}).get(codigo, f"Error desconocido ({tipo.name}-{codigo}).")
        return mensaje_base.format(**kwargs)

    @staticmethod
    def persistencia_fallida(operacion: TipoOperacion, nombre_archivo: str, causa_raiz: str) -> str:
        """
        Método de fachada que es llamado por PersistenciaException.
        Usa los códigos definidos en el diccionario MENSAJES.
        """
        # Determinar el código basado en la operación
        if operacion == TipoOperacion.GUARDADO:
            codigo_error = "GUARDADO_FALLIDO"
        elif operacion == TipoOperacion.CARGA:
            codigo_error = "CARGA_FALLIDA"
        elif operacion == TipoOperacion.LECTURA:
             codigo_error = "CARGA_FALLIDA" # Si usas LECTURA, probablemente es un error de carga
        else:
            codigo_error = "CARGA_FALLIDA" # Default, no hay un código específico para PERSISTENCIA genérica

        # Llama al método obtener, pasando los argumentos que necesita el mensaje
        return MensajeError.obtener(
            TipoOperacion.PERSISTENCIA, 
            codigo_error,
            nombre_archivo=os.path.basename(nombre_archivo),
            causa_raiz=causa_raiz
        )

# ==============================================================================
# ARCHIVO 27/68: persistencia_exception.py
# Directorio: excepciones
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/excepciones/persistencia_exception.py
# ==============================================================================

# python_forestacion/excepciones/persistencia_exception.py

import os
from python_forestacion.constantes import TipoOperacion 
# Asumo que esta clase existe y define los mensajes de error
from .mensajes_exception import MensajeError 
# Nota: No se importa ForestacionException porque PersistenciaException hereda de Exception

class PersistenciaException(Exception):
    """
    Excepción para fallos de I/O o Serialización (US-021, US-022). 
    Nota: Hereda directamente de Exception según el diseño del sistema.
    """
    
    # Asumo que estos códigos existen como constantes de clase en tu sistema.
    # Los definimos aquí temporalmente si no están en otro lado.
    COD_PERSISTENCIA_IO = "ERROR 05"
    COD_PERSISTENCIA_CORRUPTO = "ERROR 07"
    
    # Hemos adaptado el __init__ para heredar de Exception, que solo toma *args
    def __init__(self, operacion: TipoOperacion, nombre_archivo: str, causa_raiz: str, error_code: str):
        
        # Genera el mensaje legible para el usuario usando el servicio MensajeError
        user_msg = MensajeError.persistencia_fallida(operacion, nombre_archivo, causa_raiz)
        
        # Llama a Exception.__init__ con un mensaje único que combina código y user_msg
        full_message = f"[{error_code}] {user_msg} (Detalle interno: {causa_raiz})"
        super().__init__(full_message)
        
        self._tipo_operacion = operacion
        self._nombre_archivo = nombre_archivo
        self._causa_raiz = causa_raiz
        self._error_code = error_code
        self._user_message = user_msg

    # Métodos Getters
    def get_tipo_operacion(self) -> TipoOperacion:
        return self._tipo_operacion
    
    def get_nombre_archivo(self) -> str:
        return self._nombre_archivo

    def get_user_message(self) -> str:
        return self._user_message
        
    def get_error_code(self) -> str:
        return self._error_code

    # Métodos factoría para crear la excepción de forma más sencilla
    
    @classmethod
    def from_io_exception(cls, operacion: TipoOperacion, nombre_archivo: str, e: Exception):
        """Crea una excepción de Persistencia por error de I/O (ERROR 05)."""
        return cls(operacion, nombre_archivo, str(e), cls.COD_PERSISTENCIA_IO)

    @classmethod
    def from_deserialization_exception(cls, nombre_archivo: str, e: Exception):
        """Crea una excepción de Persistencia por corrupción de datos (ERROR 07)."""
        causa = f"Error de deserialización (datos incompatibles): {str(e)}"
        return cls(TipoOperacion.CARGA, nombre_archivo, causa, cls.COD_PERSISTENCIA_CORRUPTO)

    @classmethod
    def from_deserialization_exception(cls, nombre_archivo: str, e: Exception):
    # ...
    # Esto requiere que TipoOperacion.LECTURA exista.
        return cls(TipoOperacion.LECTURA, nombre_archivo, cls.COD_PERSISTENCIA_CORRUPTO)

    def __str__(self):
        # Muestra un mensaje limpio y el código
        return f"Error de Persistencia ({self._tipo_operacion.value}) {self._error_code}: {self._user_message}"

# ==============================================================================
# ARCHIVO 28/68: superficie_insuficiente_exception.py
# Directorio: excepciones
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/excepciones/superficie_insuficiente_exception.py
# ==============================================================================

from python_forestacion.constantes import TipoOperacion
from .forestacion_exception import ForestacionException

class SuperficieInsuficienteException(ForestacionException):
    """Excepción lanzada cuando no hay suficiente superficie para la plantación (US-004)."""
    
    def __init__(self, tipo_cultivo: str, requerida: float, disponible: float):
        super().__init__(
            TipoOperacion.PLANTACION, 
            "SUPERFICIE_INSUF", 
            tipo=tipo_cultivo, 
            requerida=requerida, 
            disponible=disponible
        )


################################################################################
# DIRECTORIO: patrones
################################################################################

# ==============================================================================
# ARCHIVO 29/68: __init__.py
# Directorio: patrones
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/patrones/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: patrones/factory
################################################################################

# ==============================================================================
# ARCHIVO 30/68: __init__.py
# Directorio: patrones/factory
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/patrones/factory/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 31/68: cultivo_factory.py
# Directorio: patrones/factory
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/patrones/factory/cultivo_factory.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: patrones/observer
################################################################################

# ==============================================================================
# ARCHIVO 32/68: __init__.py
# Directorio: patrones/observer
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/patrones/observer/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 33/68: observable.py
# Directorio: patrones/observer
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/patrones/observer/observable.py
# ==============================================================================

from typing import List, Generic, TypeVar
from abc import ABC
# Importar la interfaz Observer
from .observer import Observer 

# T es el tipo de dato del evento que se notifica
T = TypeVar('T') 

class Observable(Generic[T], ABC):
    """Clase base para los sujetos observables (sensores) (US-010, US-011)."""
    
    def __init__(self):
        # Ahora usa la clase Observer importada
        self._observers: List[Observer[T]] = [] 

    def add_observer(self, observer: Observer[T]):
        """Registra un observador."""
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer: Observer[T]):
        """Elimina un observador."""
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self, evento: T):
        """Notifica a todos los observadores registrados con el evento T."""
        for observer in self._observers:
            observer.update(self, evento)

# ==============================================================================
# ARCHIVO 34/68: observer.py
# Directorio: patrones/observer
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/patrones/observer/observer.py
# ==============================================================================

from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Any

# T es el tipo de dato del evento que se notifica
T = TypeVar('T') 

class Observer(Generic[T], ABC):
    """Interfaz para los observadores (US-012)."""
    @abstractmethod
    def update(self, observable: Any, evento: T):
        """Método llamado por el observable para notificar un cambio."""
        pass


################################################################################
# DIRECTORIO: patrones/observer/eventos
################################################################################

# ==============================================================================
# ARCHIVO 35/68: __init__.py
# Directorio: patrones/observer/eventos
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/patrones/observer/eventos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 36/68: evento_plantacion.py
# Directorio: patrones/observer/eventos
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/patrones/observer/eventos/evento_plantacion.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 37/68: evento_sensor.py
# Directorio: patrones/observer/eventos
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/patrones/observer/eventos/evento_sensor.py
# ==============================================================================

from typing import Literal

# Definimos los valores literales (tipos fijos) que puede tomar el sensor.
SensorValue = Literal['temperatura'] | Literal['humedad']

class EventoSensor:
    """Clase DTO (Data Transfer Object) para los datos notificados por los sensores (US-010, US-011)."""

    def __init__(self, tipo_sensor: SensorValue, lectura: float):
        self._tipo_sensor = tipo_sensor
        self._lectura = lectura
        
    def get_tipo(self) -> SensorValue: 
        return self._tipo_sensor
        
    def get_lectura(self) -> float: 
        return self._lectura


################################################################################
# DIRECTORIO: patrones/singleton
################################################################################

# ==============================================================================
# ARCHIVO 38/68: __init__.py
# Directorio: patrones/singleton
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/patrones/singleton/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 39/68: singleton.py
# Directorio: patrones/singleton
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/patrones/singleton/singleton.py
# ==============================================================================

class Singleton(object):
    """
    Clase base para implementar el Patrón Singleton (US-009).
    Asegura que solo exista una instancia de la clase.
    """
    _instance = None
    
    # 1. El __new__ maneja la creación la primera vez
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            # Nota: Esto garantiza que la instancia se crea cuando se intenta instanciar
            # Por ejemplo: CultivoServiceRegistry()
        return cls._instance

    @classmethod
    def get_instance(cls, *args, **kwargs):
        """
        Método de acceso estático. Si la instancia no existe, la crea llamando a __new__.
        Esto resuelve el error 'AttributeError: 'NoneType' object has no attribute 'registrar''
        porque garantiza que la instancia exista antes de llamar a 'registrar'.
        """
        if cls._instance is None:
            # Llama a __new__ para forzar la creación si get_instance() es el primer acceso
            cls._instance = cls.__new__(cls, *args, **kwargs)
            # Asegura que __init__ se ejecute si se está creando por primera vez
            if hasattr(cls._instance, '__init__') and not hasattr(cls._instance, '_initialized'):
                cls._instance.__init__(*args, **kwargs)
                
        return cls._instance


################################################################################
# DIRECTORIO: patrones/strategy
################################################################################

# ==============================================================================
# ARCHIVO 40/68: __init__.py
# Directorio: patrones/strategy
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/patrones/strategy/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 41/68: absorcion_agua_strategy.py
# Directorio: patrones/strategy
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/patrones/strategy/absorcion_agua_strategy.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: patrones/strategy/impl
################################################################################

# ==============================================================================
# ARCHIVO 42/68: __init__.py
# Directorio: patrones/strategy/impl
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/patrones/strategy/impl/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 43/68: absorcion_constante_strategy.py
# Directorio: patrones/strategy/impl
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/patrones/strategy/impl/absorcion_constante_strategy.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 44/68: absorcion_seasonal_strategy.py
# Directorio: patrones/strategy/impl
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/patrones/strategy/impl/absorcion_seasonal_strategy.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: riego
################################################################################

# ==============================================================================
# ARCHIVO 45/68: __init__.py
# Directorio: riego
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/riego/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: riego/control
################################################################################

# ==============================================================================
# ARCHIVO 46/68: __init__.py
# Directorio: riego/control
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/riego/control/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 47/68: control_riego_task.py
# Directorio: riego/control
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/riego/control/control_riego_task.py
# ==============================================================================

import threading
import time
from typing import Callable, Any
from python_forestacion.patrones.observer.observable import Observer # RUTA CORRECTA
from python_forestacion.patrones.observer.eventos.evento_sensor import EventoSensor # RUTA CORRECTA
from python_forestacion.constantes import UMBRAL_TEMPERATURA, UMBRAL_HUMEDAD

class ControlRiegoTask(Observer[EventoSensor], threading.Thread):
    """Controlador de riego. Implementa Observer para reaccionar a los sensores (US-012)."""
    
    def __init__(self, sensor_temp: Any, sensor_humedad: Any, riego_callback: Callable[[], Any]):
        threading.Thread.__init__(self, daemon=True)
        self._running = True
        self._sensor_temp = sensor_temp
        self._sensor_humedad = sensor_humedad
        self._riego_callback = riego_callback
        self._activo = True
        self._ultima_temp = 0.0
        self._ultima_humedad = 0.0
        
        self._sensor_temp.add_observer(self)
        self._sensor_humedad.add_observer(self)

    def update(self, observable: Any, evento: EventoSensor):
        """Método de Observer: recibe las lecturas y chequea la condición de riego (US-012)."""
        if evento.get_tipo() == "temperatura":
            self._ultima_temp = evento.get_lectura()
        elif evento.get_tipo() == "humedad":
            self._ultima_humedad = evento.get_lectura()

        self._verificar_y_ejecutar_riego()

    def _verificar_y_ejecutar_riego(self):
        if self._ultima_temp > UMBRAL_TEMPERATURA and self._ultima_humedad < UMBRAL_HUMEDAD:
            print(f"\n[CONTROLADOR RIEGO]: ¡CONDICIÓN DE RIEGO DETECTADA!")
            print(f"  -> Temp: {self._ultima_temp}°C (>{UMBRAL_TEMPERATURA}°) | Hum: {self._ultima_humedad}% (<{UMBRAL_HUMEDAD}%)")
            
            try:
                self._riego_callback() 
            except Exception as e:
                print(f"[CONTROLADOR RIEGO ERROR]: Falló el riego: {e}")
            
            self._ultima_temp = 0.0
            self._ultima_humedad = 100.0
            time.sleep(1)

    def run(self):
        while self._activo:
            # lógica de riego
            pass

    def detener(self):
        self._activo = False



################################################################################
# DIRECTORIO: riego/sensores
################################################################################

# ==============================================================================
# ARCHIVO 48/68: __init__.py
# Directorio: riego/sensores
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/riego/sensores/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 49/68: humedad_reader_task.py
# Directorio: riego/sensores
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/riego/sensores/humedad_reader_task.py
# ==============================================================================

import threading
import time
import random
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.patrones.observer.eventos.evento_sensor import EventoSensor
from python_forestacion.constantes import TIEMPO_LECTURA_SENSOR

class HumedadReaderTask(Observable[EventoSensor], threading.Thread):
    """Simula un sensor de humedad, notifica a los observadores (US-011)."""
    
    def __init__(self, controlador):  # ← AGREGADO: recibe controlador
        Observable.__init__(self)
        threading.Thread.__init__(self, daemon=True)
        self._running = True
        self._lectura_actual = 50.0
        self._controlador = controlador  # ← AGREGADO
    
    def run(self):
        """Método principal del hilo - ejecuta el ciclo de lectura"""
        print(f"[SENSOR HUMEDAD]: Sensor de humedad iniciado.")
        while self._running:
            # Leer humedad simulada
            self._lectura_actual = round(random.uniform(35.0, 65.0), 1)
            
            # Crear evento y notificar
            evento = EventoSensor("humedad", self._lectura_actual)
            self.notify_observers(evento)
            
            print(f"[SENSOR HUMEDAD]: Lectura de {self._lectura_actual}%. Notificando...")
            time.sleep(TIEMPO_LECTURA_SENSOR * 1.5)
        
        print("[SENSOR HUMEDAD]: Sensor detenido.")
    
    def detener(self):
        """Detiene el hilo de forma segura"""
        self._running = False
    
    def leer_humedad(self):
        """Devuelve la última lectura de humedad"""
        return self._lectura_actual

# ==============================================================================
# ARCHIVO 50/68: temperatura_reader_task.py
# Directorio: riego/sensores
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/riego/sensores/temperatura_reader_task.py
# ==============================================================================

import threading
import time
import random
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.patrones.observer.eventos.evento_sensor import EventoSensor
from python_forestacion.constantes import TIEMPO_LECTURA_SENSOR

class TemperaturaReaderTask(Observable[EventoSensor], threading.Thread):
    """Simula un sensor de temperatura, notifica a los observadores (US-010)."""
    
    def __init__(self, controlador):
        Observable.__init__(self)
        threading.Thread.__init__(self, daemon=True)
        self._running = True
        self._lectura_actual = 20.0
        self._controlador = controlador
    
    def run(self):
        """Método principal del hilo - ejecuta el ciclo de lectura"""
        print(f"[SENSOR TEMP]: Sensor de temperatura iniciado.")
        while self._running:
            # Leer temperatura simulada
            self._lectura_actual = round(random.uniform(18.0, 32.0), 1)
            
            # Crear evento y notificar
            evento = EventoSensor("temperatura", self._lectura_actual)
            self.notify_observers(evento)
            
            print(f"[SENSOR TEMP]: Lectura de {self._lectura_actual}°C. Notificando...")
            time.sleep(TIEMPO_LECTURA_SENSOR)
        
        print("[SENSOR TEMP]: Sensor detenido.")
    
    def detener(self):
        """Detiene el hilo de forma segura"""
        self._running = False
    
    def leer_temperatura(self):
        """Devuelve la última lectura de temperatura"""
        return self._lectura_actual


################################################################################
# DIRECTORIO: servicios
################################################################################

# ==============================================================================
# ARCHIVO 51/68: __init__.py
# Directorio: servicios
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/servicios/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: servicios/cultivos
################################################################################

# ==============================================================================
# ARCHIVO 52/68: __init__.py
# Directorio: servicios/cultivos
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/servicios/cultivos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 53/68: arbol_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/servicios/cultivos/arbol_service.py
# ==============================================================================

# Contenido de python_forestacion/servicios/cultivos/arbol_service.py

# Usar importación RELATIVA para módulos dentro del mismo paquete 'cultivos'
from .cultivo_service import CultivoService 

class ArbolService(CultivoService):
    """
    Servicio base para todos los cultivos de tipo árbol (Pino, Olivo).
    """
    
    def __init__(self, estrategia_absorcion):
        super().__init__(estrategia_absorcion)

    def crecer(self, arbol, incremento_metros):
        """Lógica de crecimiento común a todos los árboles."""
        nueva_altura = arbol.get_altura_metros() + incremento_metros
        arbol.set_altura_metros(nueva_altura)
        
    pass

# ==============================================================================
# ARCHIVO 54/68: cultivo_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/servicios/cultivos/cultivo_service.py
# ==============================================================================

from abc import ABC, abstractmethod
# 2. USAR EL NOMBRE CORRECTO DE LA CLASE: EstrategiaAbsorcion
from python_forestacion.patrones.strategy.absorcion_agua_strategy import EstrategiaAbsorcion 

# 3. Importar las implementaciones de estrategia (para que los hijos puedan inicializarse)
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy

class CultivoService(ABC):
    """Clase base abstracta para todos los servicios de cultivo."""

    # El constructor ahora debe esperar el tipo correcto:
    def __init__(self, estrategia_absorcion: EstrategiaAbsorcion):
        self._estrategia_absorcion = estrategia_absorcion
    
    # CRÍTICO: El método abstracto que todos los hijos deben implementar
    @abstractmethod
    def mostrar_info(self, cultivo) -> None:
        """Muestra información detallada del cultivo."""
        pass
    # En python_forestacion/servicios/cultivos/cultivo_service.py
def regar(self, cultivo):
    """Usa la estrategia para calcular la absorción."""
    # El método absorber_agua DEBE retornar un float.
    agua_a_absorber = self._estrategia_absorcion.absorber_agua(cultivo) 
    # Aquí se hace la lógica de riego y se le suma al cultivo si es necesario.
    # cultivo.set_agua(cultivo.get_agua_actual() + agua_a_absorber) 
    return agua_a_absorber
        
    def mostrar_info_base(self, cultivo):
        print(f"  Cultivo: {cultivo.get_nombre()}, Agua: {cultivo.get_agua_actual()} L")

# ==============================================================================
# ARCHIVO 55/68: cultivo_service_registry.py
# Directorio: servicios/cultivos
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/servicios/cultivos/cultivo_service_registry.py
# ==============================================================================

from python_forestacion.patrones.singleton.singleton import Singleton
from typing import Any, TYPE_CHECKING
from python_forestacion.entidades.cultivos.cultivo import Cultivo

# CRÍTICO: Importación Diferida (para evitar problemas de ruta/ciclos)
if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion
    from typing import Dict

class CultivoServiceRegistry(Singleton):
    """
    Registro Singleton para los servicios de cultivo concretos (US-009).
    Asegura que solo haya una instancia y centraliza la resolución de servicios.
    """
    def __init__(self):
        # Usamos un flag para garantizar que la inicialización solo ocurra una vez
        if not hasattr(self, '_initialized'):
            self._registro: Dict[str, Any] = {}
            self._initialized = True
            print("[REGISTRY]: CultivoServiceRegistry inicializado.")
    
    def registrar(self, tipo_cultivo: str, servicio_instance: Any):
        """Registra una instancia de servicio concreto (ej: PinoService)."""
        tipo_cultivo = tipo_cultivo.lower()
        if tipo_cultivo not in self._registro:
            self._registro[tipo_cultivo] = servicio_instance
    
    def obtener_servicio(self, tipo_cultivo: str) -> Any:
        """Devuelve la instancia del servicio de cultivo para un tipo dado."""
        tipo_cultivo = tipo_cultivo.lower()
        servicio = self._registro.get(tipo_cultivo)
        if not servicio:
            raise ValueError(f"Servicio no encontrado para el tipo de cultivo: {tipo_cultivo}")
        return servicio
    
    def mostrar_datos(self, plantacion: 'Plantacion'):
        self.mostrar_info(plantacion)
    
    def mostrar_datos_resumidos(self, cultivo):
        """Muestra datos resumidos de un cultivo individual"""
        print(f"    Tipo: {type(cultivo).__name__}")
        print(f"    Superficie: {cultivo.get_superficie():.2f} m²")
        print(f"    Agua: {cultivo.get_agua():.2f} L")  # ← CORREGIDO: get_agua() en lugar de get_agua_disponible()
    
    def mostrar_info(self, plantacion: 'Plantacion'):
        """Muestra información detallada de los cultivos."""
        print("--- REPORTE FINAL DE CULTIVOS EN PLANTACIÓN ---")
        cultivos_a_mostrar = plantacion.get_cultivos()
        for cultivo in cultivos_a_mostrar:
            print(f" [Info Cultivo {cultivo.get_id()}] - {cultivo.get_nombre()}: Agua: {cultivo.get_agua():.2f} L")

# ==============================================================================
# ARCHIVO 56/68: lechuga_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/servicios/cultivos/lechuga_service.py
# ==============================================================================

from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.entidades.cultivos.lechuga import Lechuga
# Asumo que tienes el CultivoServiceRegistry
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry 

class LechugaService(CultivoService):
    """Servicio para la gestión y visualización del cultivo de Lechuga."""

    def __init__(self):
        # La lechuga usa absorción constante (ejemplo: 0.5 litros)
        super().__init__(AbsorcionConstanteStrategy(cantidad_constante=0.5))

    # Implementación CRÍTICA del método abstracto
    def mostrar_info(self, cultivo: Lechuga) -> None:
        """Muestra los datos específicos de la lechuga."""
        
        # Llama a la lógica base (si CultivoService tiene implementación, si no, puedes omitirlo)
        super().mostrar_datos(cultivo)
        
        # Muestra los datos únicos de Lechuga
        print(f"  -> Servicio Lechuga: Variedad='{cultivo.get_variedad()}', Peso promedio={cultivo.get_peso_unidad()} kg.")

# Registro del servicio en el Singleton (CRÍTICO para que la importación en main.py funcione)
CultivoServiceRegistry.get_instance().registrar("Lechuga", LechugaService())


# ==============================================================================
# ARCHIVO 57/68: olivo_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/servicios/cultivos/olivo_service.py
# ==============================================================================

from .cultivo_service import CultivoService
from .cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.entidades.cultivos.olivo import Olivo
# Importamos la estrategia correcta para Olivos (árboles)
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy

class OlivoService(CultivoService):
    """Lógica de negocio específica para el cultivo Olivo."""
    
    # CRÍTICO: IMPLEMENTACIÓN DEL CONSTRUCTOR FALTANTE
    def __init__(self):
        # Los Olivos, como árboles, usan la estrategia estacional.
        # Esto resuelve el TypeError que viste en la última traza.
        super().__init__(AbsorcionSeasonalStrategy())
    
    # ÚNICA definición de mostrar_info
    def mostrar_info(self, cultivo: Olivo):
        """Muestra información detallada del Olivo."""
        if not isinstance(cultivo, Olivo):
             raise TypeError("El cultivo debe ser una instancia de Olivo.")
        
        # Esta línea causará un AttributeError si get_edad() no está en Arbol.py
        print(f"  -> Servicio Olivo: Aceituna={cultivo.get_tipo_aceituna().value}, Edad={cultivo.get_edad()} años.") 

# --- REGISTRO DE SERVICIO (CRÍTICO PARA US-009) ---
# Esto ahora llamará al __init__ corregido.
CultivoServiceRegistry.get_instance().registrar("Olivo", OlivoService())

# ==============================================================================
# ARCHIVO 58/68: pino_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/servicios/cultivos/pino_service.py
# ==============================================================================

from .cultivo_service import CultivoService
from .cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.constantes import AGUA_INICIAL_PINO, SUPERFICIE_PINO
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy

class PinoService(CultivoService):
    """Lógica de negocio específica para el cultivo Pino."""
    
def mostrar_info(self, cultivo: Pino) -> None:
    super().mostrar_datos(cultivo)
    super().__init__(AbsorcionSeasonalStrategy())
    print(f"  -> Servicio Pino: Variedad={cultivo.get_variedad()}, Altura={cultivo.get_altura_metros()}m.")




# ==============================================================================
# ARCHIVO 59/68: zanahoria_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/servicios/cultivos/zanahoria_service.py
# ==============================================================================

from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry # Debe estar para el registro
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy

class ZanahoriaService(CultivoService):
    """Lógica de negocio específica para el cultivo Zanahoria."""
    
    # ✅ CORRECTO: IMPLEMENTAR EL CONSTRUCTOR
    def __init__(self):
        # La Zanahoria usa absorción constante. Esto resuelve el TypeError.
        super().__init__(AbsorcionConstanteStrategy(cantidad_constante=0.3)) 

    # ✅ CORRECTO: IMPLEMENTAR EL MÉTODO ABSTRACTO (mostrar_info o mostrar_datos, debe ser consistente)
    # NOTA: Asumo que el método correcto es 'mostrar_info', como en LechugaService.
    def mostrar_info(self, cultivo: Zanahoria) -> None:
        """Muestra información detallada de la Zanahoria."""
        
        # Debes llamar al método base, usando el nombre que CultivoService espera (mostrar_info_base)
        super().mostrar_info_base(cultivo) # O super().mostrar_info(cultivo)
        
        tipo = "Baby Carrot" if cultivo.es_baby_carrot() else "Común"
        print(f"  -> Servicio Zanahoria: Tipo={tipo}")

# --- REGISTRO DE SERVICIO (CRÍTICO) ---
CultivoServiceRegistry.get_instance().registrar("Zanahoria", ZanahoriaService())


################################################################################
# DIRECTORIO: servicios/negocios
################################################################################

# ==============================================================================
# ARCHIVO 60/68: __init__.py
# Directorio: servicios/negocios
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/servicios/negocios/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 61/68: fincas_service.py
# Directorio: servicios/negocios
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/servicios/negocios/fincas_service.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 62/68: paquete.py
# Directorio: servicios/negocios
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/servicios/negocios/paquete.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: servicios/personal
################################################################################

# ==============================================================================
# ARCHIVO 63/68: __init__.py
# Directorio: servicios/personal
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/servicios/personal/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 64/68: trabajador_service.py
# Directorio: servicios/personal
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/servicios/personal/trabajador_service.py
# ==============================================================================

# Archivo: python_forestacion/servicios/personal/trabajador_service.py
from typing import List
from datetime import date
from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.entidades.personal.apto_medico import AptoMedico
from python_forestacion.entidades.personal.herramienta import Herramienta
from python_forestacion.entidades.personal.tarea import EstadoTarea

class TrabajadorService:
    """Servicio para la gestión de trabajadores, tareas y aptitud médica."""

    def asignar_apto_medico(self, trabajador: Trabajador, apto: bool, fecha_emision: date, observaciones: str = None):
        """Asigna un AptoMedico al trabajador (US-015)."""
        apto_medico = AptoMedico(apto, fecha_emision, observaciones)
        trabajador.set_apto_medico(apto_medico)
        return apto_medico

    def puede_trabajar(self, trabajador: Trabajador) -> bool:
        """Verifica si el trabajador tiene apto médico válido (US-016)."""
        apto = trabajador.get_apto_medico()
        return apto is not None and apto.esta_apto()

    @staticmethod
    def _obtener_id_tarea(tarea):
        """Método estático para el ordenamiento de tareas (US-016)."""
        return tarea.get_id()

    def trabajar(self, trabajador: Trabajador, fecha: date, util: Herramienta) -> bool:
        """
        Ejecuta las tareas asignadas al trabajador para la fecha dada (US-016).
        Las tareas se ejecutan en orden ID descendente.
        """
        if not self.puede_trabajar(trabajador):
            print(f"[!] {trabajador.get_nombre()} NO puede trabajar: Sin apto medico")
            return False

        print(f"[OK] {trabajador.get_nombre()} trabajando el {fecha}")

        # 1. Obtener y ordenar tareas por ID descendente (US-016)
        tareas_pendientes = [
            t for t in trabajador.get_tareas_asignadas() 
            if t.get_estado() == EstadoTarea.PENDIENTE and t.get_fecha_programada() == fecha
        ]
        
        # Ordenamiento ID descendente (3, 2, 1)
        tareas_pendientes.sort(key=TrabajadorService._obtener_id_tarea, reverse=True) 
        
        # 2. Ejecutar y marcar como completada
        for tarea in tareas_pendientes:
            print(f"      Tarea #{tarea.get_id()}: {tarea.get_nombre()}")
            print(f"      Usando: {util.get_nombre()}")
            tarea.marcar_completada() # Aunque en esta simple simulación no modificamos la lista del trabajador

        return True


################################################################################
# DIRECTORIO: servicios/terrenos
################################################################################

# ==============================================================================
# ARCHIVO 65/68: __init__.py
# Directorio: servicios/terrenos
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/servicios/terrenos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 66/68: plantacion_service.py
# Directorio: servicios/terrenos
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/servicios/terrenos/plantacion_service.py
# ==============================================================================

from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.entidades.cultivos.cultivo import Cultivo
# Asumimos que esta ruta es correcta (Patrón Factory)
from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory 
# Asumimos que estas excepciones y constantes existen
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.constantes import AGUA_MINIMA_RIEGOS
from typing import List
# Implementación CORREGIDA del método plantar en PlantacionService
from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry

class PlantacionService:
    
    def __init__(self):
        # Es crucial que PlantacionService tenga una referencia a la Registry
        self._cultivo_registry = CultivoServiceRegistry() # O CultivoServiceRegistry.obtener_instancia()

    # CRÍTICO: Implementar el método getter para resolver el error fatal.
    def get_cultivo_service_registry(self) -> CultivoServiceRegistry:
        """Retorna la instancia del Singleton CultivoServiceRegistry."""
        return self._cultivo_registry 
    
    def plantar(self, plantacion: Plantacion, tipo_cultivo: str, cantidad: int, **kwargs):
        """
        Planta una cantidad de cultivos de un tipo específico (US-006).
        """
        factory = CultivoFactory()
        superficie_requerida = factory.calcular_superficie(tipo_cultivo, cantidad)
        
        tierra = plantacion.get_tierra()
        
        # OBTENER LA SUPERFICIE DISPONIBLE REAL
        # Asumo que la superficie total de la Tierra está en el atributo _superficie
        superficie_total = tierra._superficie 
        
        # Obtener la superficie ya ocupada por otros cultivos
        superficie_ocupada = sum(c._superficie for c in plantacion.get_cultivos())
        
        # Superficie que realmente queda libre
        superficie_disponible = superficie_total - superficie_ocupada
        
        # 3. Comprobar la disponibilidad (US-004)
        if superficie_requerida > superficie_disponible: 
            raise SuperficieInsuficienteException(
                tipo_cultivo=tipo_cultivo, 
                requerida=superficie_requerida, 
                disponible=superficie_disponible
            )
            
        # 4. Crear los cultivos y agregarlos a la plantación
        for _ in range(cantidad):
            cultivo = factory.crear_cultivo(tipo_cultivo, **kwargs)
            plantacion.add_cultivo(cultivo)
            
        print(f"[PLANTACIÓN]: {cantidad} {tipo_cultivo}(s) plantados. Superficie disponible restante: {superficie_disponible - superficie_requerida:.2f} m².")

    def _get_superficie_ocupada(self, plantacion: Plantacion) -> float:
        """Calcula la superficie total ocupada por los cultivos."""
        return sum(c.get_superficie() for c in plantacion.get_cultivos())

    def plantar(self, plantacion: Plantacion, tipo_cultivo: str, cantidad: int, **kwargs) -> List[Cultivo]:
        """
        Planta uno o varios cultivos verificando la superficie disponible (US-004).
        """
        cultivos_plantados: List[Cultivo] = []
        superficie_ocupada = self._get_superficie_ocupada(plantacion)
        superficie_disponible = plantacion.get_superficie_maxima() - superficie_ocupada
        
        # Crear un cultivo de prueba para obtener su superficie requerida
        cultivo_base = CultivoFactory.crear_cultivo(tipo_cultivo, **kwargs)
        sup_requerida_total = cultivo_base.get_superficie() * cantidad
        
        if sup_requerida_total > superficie_disponible:
            raise SuperficieInsuficienteException(
                tipo_cultivo, sup_requerida_total, superficie_disponible
            )
            
        for i in range(cantidad):
            # Crea la instancia real con el Factory
            nuevo_cultivo = CultivoFactory.crear_cultivo(tipo_cultivo, **kwargs)
            nuevo_cultivo.set_id(len(plantacion.get_cultivos()) + 1)
            plantacion._cultivos.append(nuevo_cultivo)
            cultivos_plantados.append(nuevo_cultivo)
            
        print(f"Plantados {cantidad} {tipo_cultivo}(s) en '{plantacion._nombre}'. Superficie total ocupada: {self._get_superficie_ocupada(plantacion):.2f} m².")
        return cultivos_plantados

    def regar(self, plantacion: Plantacion):
        """
        Simula la absorción de agua por todos los cultivos y consume agua de la plantación (US-008).
        """
        agua_disponible = plantacion.get_agua_disponible()
        
        if agua_disponible < AGUA_MINIMA_RIEGOS:
            raise AguaAgotadaException(agua_disponible)
            
        agua_consumida_total = 0
        
        for cultivo in plantacion.get_cultivos():
            agua_antes = cultivo.get_agua()
            
            # Ejecución del Patrón Strategy (US-008)
            cultivo.get_estrategia().absorber_agua(cultivo) 
            
            agua_despues = cultivo.get_agua()
            agua_consumida = agua_despues - agua_antes
            agua_consumida_total += agua_consumida
            
        # Consumir el agua del tanque de la Plantación
        plantacion.set_agua_disponible(plantacion.get_agua_disponible() - agua_consumida_total)
        
        print(f"Riego completado en '{plantacion._nombre}'. Consumo total: {agua_consumida_total} L. Agua restante: {plantacion.get_agua_disponible()} L.")

# ==============================================================================
# ARCHIVO 67/68: registro_forestal_service.py
# Directorio: servicios/terrenos
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/servicios/terrenos/registro_forestal_service.py
# ==============================================================================

# Archivo: python_forestacion/servicios/terrenos/registro_forestal_service.py
# ESTE ARCHIVO DEBE CONTENER LA CLASE SERVICIO 'RegistroForestalService'

import pickle
import os
from typing import Dict, Any
import copy
# CRÍTICO: PersistenciaException hereda de Exception, no de ForestacionException, pero la importamos.
# Asumo que TipoOperacion se importa correctamente desde constantes.
from python_forestacion.excepciones.persistencia_exception import PersistenciaException
from python_forestacion.constantes import DIRECTORIO_DATA, EXTENSION_DATA, TipoOperacion # TipoOperacion debe estar aquí
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal

class RegistroForestalService: 
    """
    Servicio para la persistencia de datos (Guardar/Cargar estado) (US-021, US-022).
    También maneja el reporte de datos completo (US-023).
    """

    def __init__(self, nombre_archivo_base: str = "registro_simulacion"):
        self.DATA_DIR = DIRECTORIO_DATA # "data"
        self._nombre_archivo_base = nombre_archivo_base 
        self._ruta_archivo = os.path.join(self.DATA_DIR, f"{self._nombre_archivo_base}{EXTENSION_DATA}")

        if not os.path.exists(self.DATA_DIR):
            os.makedirs(self.DATA_DIR)

    # --- Persistencia (US-021, US-022) ---

    def persistir(self, registro: RegistroForestal):
        """Guarda el objeto RegistroForestal completo usando pickle (US-021)."""
        try:
            with open(self._ruta_archivo, 'wb') as f: 
                pickle.dump(registro, f)
            print(f"[PERSISTENCIA]: Registro de {registro.get_propietario()} persistido exitosamente en {self._ruta_archivo}") 
        except Exception as e:
            # LLAMADA CORREGIDA: Usando la firma de 4 argumentos: (operacion, nombre_archivo, causa_raiz, error_code)
            raise PersistenciaException(
                operacion=TipoOperacion.GUARDADO,  # Usamos GUARDADO
                nombre_archivo=self._ruta_archivo,
                causa_raiz=str(e),
                error_code=PersistenciaException.COD_PERSISTENCIA_IO # Asumo que COD_PERSISTENCIA_IO existe en PersistenciaException
            )

    @staticmethod
    def leer_registro(nombre_archivo_base: str) -> RegistroForestal:
        """Carga el objeto RegistroForestal completo desde disco (US-022). (Método estático)"""
        ruta_archivo = os.path.join(DIRECTORIO_DATA, f"{nombre_archivo_base}{EXTENSION_DATA}")

        if not os.path.exists(ruta_archivo):
            # LLAMADA CORREGIDA: Usando el método factoría para archivos no encontrados
            raise PersistenciaException(
                operacion=TipoOperacion.CARGA, # Usamos CARGA
                nombre_archivo=ruta_archivo,
                causa_raiz="Archivo no encontrado",
                error_code=PersistenciaException.COD_PERSISTENCIA_IO
            )

        try:
            with open(ruta_archivo, 'rb') as f: 
                registro: RegistroForestal = pickle.load(f)

            print(f"[PERSISTENCIA]: Registro de {registro.get_propietario()} recuperado exitosamente desde {ruta_archivo}")
            return registro
        except (IOError, pickle.UnpicklingError, EOFError) as e:
            # LLAMADA CORREGIDA: Usando el método factoría para errores de deserialización
            # Si tienes un método from_deserialization_exception, úsalo:
            if hasattr(PersistenciaException, 'from_deserialization_exception'):
                raise PersistenciaException.from_deserialization_exception(nombre_archivo=ruta_archivo, e=e)
            else:
                # Si no existe, usamos la llamada directa:
                raise PersistenciaException(
                    operacion=TipoOperacion.CARGA, # Usamos CARGA
                    nombre_archivo=ruta_archivo,
                    causa_raiz=f"Corrupción/Vacío. Detalle: {str(e)}",
                    error_code=PersistenciaException.COD_PERSISTENCIA_CORRUPTO
                )

    # --- Reporte (US-023) ---

    def mostrar_datos(self, registro: RegistroForestal):
        """
        Muestra todos los datos de un registro forestal en formato legible (US-023).
        """
        plantacion = registro.get_plantacion()
        
        # ... (el resto del código de mostrar_datos es correcto y no requiere cambios) ...
        
        print("\n" + "=" * 33)
        print("REGISTRO FORESTAL".center(33))
        print("=" * 33)
        print(f"Padron:      {registro.get_id_padron()}")
        print(f"Propietario: {registro.get_propietario()}")
        print(f"Avaluo:      {registro.get_avaluo():.2f}")
        print(f"Domicilio:   {registro.get_tierra().get_domicilio()}")
        print(f"Superficie:  {registro.get_tierra().get_superficie():.2f} m²")
        print(f"Cultivos:    {len(plantacion.get_cultivos())} plantados")
        print(f"Agua Disp.:  {plantacion.get_agua_disponible():.2f} L")
        print(f"Superficie Ocupada: {plantacion.get_superficie_ocupada():.2f} m²")

        # Sección de Cultivos (US-023)
        print("\n" + "-" * 33)
        print("LISTADO DE CULTIVOS".center(33))
        print("-" * 33)
        registry = CultivoServiceRegistry.get_instance()

        for cultivo in plantacion.get_cultivos():
            registry.mostrar_datos_resumidos(cultivo) 
            print("-" * 15) 

        # Sección de Trabajadores (US-023)
        print("\n" + "-" * 33)
        print("PERSONAL ASIGNADO".center(33))
        print("-" * 33)
        for trabajador in plantacion.get_trabajadores():
            print(f"    {trabajador}")

# ==============================================================================
# ARCHIVO 68/68: tierra_service.py
# Directorio: servicios/terrenos
# Ruta completa: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/servicios/terrenos/tierra_service.py
# ==============================================================================

# python_forestacion/servicios/terrenos/tierra_service.py

# --- Importaciones de Entidades (Correcto) ---
from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion

class TierraService:
    """
    Servicio de gestión de la entidad Tierra y la creación de Plantaciones iniciales.
    """

    # CRÍTICO: El método debe estar indentado DENTRO de la clase TierraService
    def crear_tierra_con_plantacion(
        self, 
        id_padron: int, 
        superficie: float, 
        domicilio: str, 
        nombre_plantacion: str, 
        agua_inicial: float 
    ) -> Tierra:
        """
        Crea una instancia de Tierra y le asigna una Plantacion.
        Este método soluciona el error del argumento 'agua_inicial' que salió anteriormente.
        """
        
        # 1. Crear Plantacion (ahora pasándole el agua inicial)
        plantacion = Plantacion(
            id_padron=id_padron,
            domicilio=domicilio,
            superficie=superficie, # La Plantacion toma la superficie de la Tierra
            nombre_plantacion=nombre_plantacion,
            agua_inicial=agua_inicial # Se usa el valor pasado como argumento
        )
        
        # 2. Crear Tierra
        tierra = Tierra(
            id_padron=id_padron,
            superficie=superficie,
            domicilio=domicilio
        )
        
        # 3. Asignar Plantacion a Tierra
        tierra.set_finca(plantacion)

        return tierra

    # Puedes agregar otros métodos aquí si son necesarios
    # def algun_otro_metodo(self, ...):
    #     pass


################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 68
# Generado: 2025-10-22 10:21:44
################################################################################
