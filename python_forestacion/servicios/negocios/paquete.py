from typing import Generic, TypeVar, Optional
from datetime import datetime

# T es el tipo de datos que encapsula el paquete (Cultivo o Plantacion)
T = TypeVar('T', bound=object) 
# No se necesitan imports de Cultivo o Plantacion si solo se usa 'T'

class Paquete(Generic[T]):
    """
    Entidad Paquete (DTO) que encapsula un Cultivo o una Plantacion (US-018).
    Se ubica aquí siguiendo la estructura provista.
    """
    
    def __init__(self, elemento: T, etiqueta: Optional[str] = None):
        self._elemento: T = elemento
        self._etiqueta = etiqueta 
        self._fecha_creacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_elemento(self) -> T:
        return self._elemento
        
    def __str__(self) -> str:
        # Usa elemento.__class__.__name__ para obtener el nombre de la clase
        return (f"Paquete [{self._elemento.__class__.__name__}] (Fecha: {self._fecha_creacion}, "
                f"Etiqueta: {self._etiqueta if self._etiqueta else 'N/A'})")