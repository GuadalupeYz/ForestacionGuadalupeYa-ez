from typing import Optional, TYPE_CHECKING
# Usamos TYPE_CHECKING y comillas para romper dependencias circulares y evitar warnings
if TYPE_CHECKING:
    from .plantacion import Plantacion

class Tierra:
    """Entidad Tierra (Terreno) (US-001)."""
    
    def __init__(self, id_padron_catastral: int, superficie: float, domicilio: str):
        self._id_padron_catastral = id_padron_catastral
        self._superficie = superficie
        self._domicilio = domicilio
        self._finca: Optional['Plantacion'] = None # Usamos comillas

    def get_superficie(self) -> float: 
        return self._superficie
    
    def set_finca(self, plantacion: 'Plantacion'): self._finca = plantacion # Usamos comillas
    def get_finca(self) -> Optional['Plantacion']: return self._finca # Usamos comillas
    # ... (Otros getters necesarios)