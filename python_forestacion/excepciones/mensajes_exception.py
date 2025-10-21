from python_forestacion.constantes import TipoOperacion
from typing import Dict, Any

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
            "CARGA_FALLIDA": "Error al cargar el registro '{nombre_archivo}'. El archivo está corrupto o vacío.",
            "GUARDADO_FALLIDO": "Error al guardar el estado del sistema en '{nombre_archivo}'."
        }
    }

    @staticmethod
    def obtener(tipo: TipoOperacion, codigo: str, **kwargs) -> str:
        """Obtiene y formatea un mensaje de error según el tipo y código."""
        mensaje_base = MensajeError.MENSAJES.get(tipo, {}).get(codigo, "Error desconocido.")
        return mensaje_base.format(**kwargs)