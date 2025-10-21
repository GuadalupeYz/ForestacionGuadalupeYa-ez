# python_forestacion/excepciones/persistencia_exception.py
from .forestacion_exception import ForestacionException
from .mensajes_exception import MensajeError
from python_forestacion.constantes import TipoOperacion
import os

class PersistenciaException(ForestacionException):
    """Excepción para fallos de I/O o Serialización (US-021, US-022)."""
    def __init__(self, operacion: TipoOperacion, nombre_archivo: str, causa_raiz: str, error_code: str):
        user_msg = MensajeError.persistencia_fallida(operacion, os.path.basename(nombre_archivo), causa_raiz)
        super().__init__(error_code, user_msg, internal_detail=causa_raiz)
        self._tipo_operacion = operacion
        self._nombre_archivo = nombre_archivo

    def get_tipo_operacion(self) -> TipoOperacion:
        return self._tipo_operacion
    
    def get_nombre_archivo(self) -> str:
        return self._nombre_archivo

    @staticmethod
    def from_io_exception(operacion: TipoOperacion, nombre_archivo: str, e: Exception):
        """Crea una excepción de Persistencia por error de I/O (ERROR 05)."""
        return PersistenciaException(operacion, nombre_archivo, str(e), ForestacionException.COD_PERSISTENCIA_IO)

    @staticmethod
    def from_deserialization_exception(nombre_archivo: str, e: Exception):
        """Crea una excepción de Persistencia por corrupción de datos (ERROR 07)."""
        causa = f"Error de deserialización (datos incompatibles): {str(e)}"
        return PersistenciaException(TipoOperacion.LECTURA, nombre_archivo, causa, ForestacionException.COD_PERSISTENCIA_CORRUPTO)