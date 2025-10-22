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