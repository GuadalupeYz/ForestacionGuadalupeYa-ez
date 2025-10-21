from datetime import date

class AptoMedico:
    """Entidad que certifica la aptitud del trabajador (US-014)."""
    
    def __init__(self, fecha_vencimiento: date):
        self._fecha_emision = date.today()
        self._fecha_vencimiento = fecha_vencimiento