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