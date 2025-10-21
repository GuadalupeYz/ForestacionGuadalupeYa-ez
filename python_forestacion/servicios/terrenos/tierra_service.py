# Importamos la Entidad Tierra y Plantacion
from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion

class TierraService:
    """Servicio para la gestión de la entidad Tierra (US-001)."""

    def crear_tierra_con_plantacion(self, id_padron: int, superficie: float, 
                                     domicilio: str, nombre_plantacion: str) -> Tierra:
        """Crea una Tierra y asocia una Plantación inmediatamente."""
        tierra = Tierra(id_padron, superficie, domicilio)
        # La Plantación toma la superficie de la Tierra como su capacidad máxima
        plantacion = Plantacion(nombre_plantacion, superficie) 
        
        # Lógica de negocio: enlaza bidireccionalmente la Tierra con la Plantación
        tierra.set_finca(plantacion)
        plantacion.set_tierra(tierra)
        
        return tierra