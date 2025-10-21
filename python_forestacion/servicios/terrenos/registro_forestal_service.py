import pickle
import os
from typing import Dict, Any

from python_forestacion.excepciones.persistencia_exception import PersistenciaException

class RegistroForestalService:
    """
    Servicio para la persistencia de datos (Guardar/Cargar estado) (US-021, US-022).
    """

    def __init__(self, nombre_base: str):
        # Usamos un directorio 'data/' para almacenar los archivos .dat
        self.DATA_DIR = "data"
        if not os.path.exists(self.DATA_DIR):
            os.makedirs(self.DATA_DIR)
            
        self._nombre_archivo = os.path.join(self.DATA_DIR, f"{nombre_base}.dat")

    def guardar_registro(self, estado: Dict[str, Any]):
        """Guarda el estado completo del sistema usando pickle (US-021)."""
        try:
            with open(self._nombre_archivo, 'wb') as f:
                pickle.dump(estado, f)
            print(f"[PERSISTENCIA]: Estado del sistema guardado en {self._nombre_archivo}")
        except Exception as e:
            # Asumo que existe PersistenciaException para un manejo controlado
            raise PersistenciaException(f"Guardado fallido: {e}") 

    def cargar_registro(self) -> Dict[str, Any]:
        """Carga el estado del sistema, devolviendo un diccionario vacío si falla o no existe (US-022)."""
        if not os.path.exists(self._nombre_archivo):
            print(f"[PERSISTENCIA]: Archivo no encontrado. Iniciando sistema nuevo.")
            return {}
        
        try:
            with open(self._nombre_archivo, 'rb') as f:
                estado = pickle.load(f)
            print(f"[PERSISTENCIA]: Estado cargado exitosamente desde {self._nombre_archivo}")
            return estado
        except Exception as e:
            print(f"[PERSISTENCIA ERROR]: Fallo al cargar el archivo. Iniciando sistema nuevo. Error: {e}")
            return {}