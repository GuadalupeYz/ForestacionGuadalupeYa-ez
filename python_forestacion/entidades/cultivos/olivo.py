# En python_forestacion/entidades/cultivos/olivo.py
from .arbol import Arbol
from .tipo_aceituna import TipoAceituna
from python_forestacion.constantes import SUPERFICIE_OLIVO, AGUA_INICIAL_OLIVO

class Olivo(Arbol):
    """Cultivo concreto: Olivo (US-006)."""
    # Constructor ÚNICO y CORRECTO
    def __init__(self, tipo_aceituna: TipoAceituna, edad: int = 5, **kwargs):
        # Llama al constructor de Arbol, pasando todos los parámetros necesarios.
        # Aquí también se inicializa self._edad en la clase base Arbol.
        super().__init__(
            nombre="Olivo", 
            edad=edad, 
            superficie=SUPERFICIE_OLIVO, # Usar la constante aquí si es preferible
            agua_inicial=AGUA_INICIAL_OLIVO, # Pasar agua inicial si Arbol lo acepta
            **kwargs
        ) 

        self._tipo_aceituna = tipo_aceituna
        # NO NECESITAS self._edad = edad aquí, ya que Arbol ya lo hace.

    def get_tipo_aceituna(self) -> TipoAceituna: 
        return self._tipo_aceituna

    def __str__(self) -> str:
        return f"Olivo (Tipo Aceituna: {self._tipo_aceituna.value}, Edad: {self.get_edad()} años)"
    
    def get_edad(self) -> int:
        """Devuelve la edad del árbol. El atributo _edad se inicializa en la clase Arbol."""
        return self._edad