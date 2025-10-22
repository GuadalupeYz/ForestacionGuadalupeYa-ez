from .hortaliza import Hortaliza
from python_forestacion.constantes import SUPERFICIE_ZANAHORIA, AGUA_INICIAL_ZANAHORIA

class Zanahoria(Hortaliza):
    def __init__(self, **kwargs):
        # 1. Extraer los parámetros específicos con valores por defecto
        self._es_baby_carrot = kwargs.pop('es_baby_carrot', False)
        self._longitud = kwargs.pop('longitud', 0.15)  # valor por defecto razonable

        # 2. Llamar a la clase padre (Hortaliza)
        super().__init__(
            nombre="Zanahoria",
            agua_inicial=AGUA_INICIAL_ZANAHORIA,
            superficie=SUPERFICIE_ZANAHORIA,
            **kwargs
        )

    def es_baby_carrot(self) -> bool:
        return self._es_baby_carrot

    def get_longitud(self) -> float:
        return self._longitud

    def __str__(self) -> str:
        tipo = "Baby Carrot" if self._es_baby_carrot else "Zanahoria común"
        return f"{tipo} (Longitud: {self._longitud:.2f}m)"
