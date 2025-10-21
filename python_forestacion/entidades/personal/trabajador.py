from datetime import date
from typing import Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from .apto_medico import AptoMedico

class Trabajador:
    """Entidad Trabajador (US-014)."""
    
    def __init__(self, nombre: str, apellido: str, dni: int, fecha_nacimiento: date):
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
        self._fecha_nacimiento = fecha_nacimiento
        self._apto_medico: Optional['AptoMedico'] = None

    def get_apto_medico(self) -> Optional['AptoMedico']: return self._apto_medico
    def set_apto_medico(self, apto: 'AptoMedico'): self._apto_medico = apto