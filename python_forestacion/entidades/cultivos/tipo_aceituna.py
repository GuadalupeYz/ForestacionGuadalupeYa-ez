from enum import Enum

class TipoAceituna(Enum):
    """Enum para los tipos de aceituna del Olivo."""
    MANZANILLA = "Manzanilla"
    ARBEQUINA = "Arbequina"
    PICUAL = "Picual"
    def __str__ (self):
        return self.value