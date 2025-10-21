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