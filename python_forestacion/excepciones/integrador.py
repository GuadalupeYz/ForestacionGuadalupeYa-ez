"""
Archivo integrador generado automaticamente
Directorio: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/excepciones
Fecha: 2025-10-22 10:21:44
Total de archivos integrados: 6
"""

# ================================================================================
# ARCHIVO 1/6: __init__.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/excepciones/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/6: agua_agotada_exception.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/excepciones/agua_agotada_exception.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/6: forestacion_exception.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/excepciones/forestacion_exception.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 4/6: mensajes_exception.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/excepciones/mensajes_exception.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 5/6: persistencia_exception.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/excepciones/persistencia_exception.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 6/6: superficie_insuficiente_exception.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/excepciones/superficie_insuficiente_exception.py
# ================================================================================

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

