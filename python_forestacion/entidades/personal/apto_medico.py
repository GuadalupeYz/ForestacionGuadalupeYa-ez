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