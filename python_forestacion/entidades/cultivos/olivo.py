# python_forestacion/entidades/cultivos/olivo.py
from .arbol import Arbol
from .tipo_aceituna import TipoAceituna 
# ELIMINAR CUALQUIER OTRA IMPORTACIÓN DE TIPOACEITUNA
from python_forestacion.constantes import SUPERFICIE_OLIVO, AGUA_INICIAL_OLIVO

class Olivo(Arbol):
    
    def __init__(self, **kwargs):
        
        # 1. Extraer y preparar el Enum ANTES de llamar a super()
        variedad_str = kwargs.pop('variedad', kwargs.pop('tipo_aceituna', 'MANZANILLA'))
        
        try:
             # Aquí variedad_enum es temporal
             variedad_enum = TipoAceituna[variedad_str.upper()]
        except KeyError:
             variedad_enum = TipoAceituna.MANZANILLA
        
        # 2. Asignar el atributo específico del Olivo
        # ¡IMPORTANTE! Lo ponemos aquí para que el objeto se "complete" antes del super si es posible.
        self._tipo_aceituna = variedad_enum 

        # 3. Llamar a la clase padre (Arbol)
        super().__init__(
            nombre="Olivo",
            agua_inicial=kwargs.pop('agua_inicial', AGUA_INICIAL_OLIVO),
            superficie=kwargs.pop('superficie', SUPERFICIE_OLIVO),
            **kwargs 
        )

    # 4. Implementación CRÍTICA del método abstracto
    # Asegúrate de que no tenga @abstractmethod y tenga 4 espacios de indentación
    def __str__(self) -> str:
        return f"Olivo (Tipo Aceituna: {self._tipo_aceituna.value}, Edad: {self.get_edad_anios()} años)"

    # --- Getters ---

    def get_variedad(self) -> TipoAceituna:
        return self._tipo_aceituna

    def get_tipo_aceituna(self):
        return self._tipo_aceituna
