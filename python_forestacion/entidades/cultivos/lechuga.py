from .hortaliza import Hortaliza
from python_forestacion.constantes import SUPERFICIE_LECHUGA, AGUA_INICIAL_LECHUGA
# Contenido CORREGIDO y CONSISTENTE en lechuga.py

class Lechuga(Hortaliza):
    def __init__(self, **kwargs): 
        peso = kwargs.pop('peso', 1.0)
        variedad = kwargs.pop('variedad', 'Desconocida')
        super().__init__(
            nombre="Lechuga",
            agua_inicial=AGUA_INICIAL_LECHUGA,
            superficie=SUPERFICIE_LECHUGA,
            **kwargs
        )
        self._peso_unidad = peso
        self._variedad = variedad

    # 3. Getter para el peso (usado en la cosecha y visualización)
    def get_peso(self) -> float:
        return self._peso_unidad
        
    # 4. Getter para la variedad (usado en el Service)
    def get_variedad(self) -> str:
        return self._variedad
        
    def __str__(self) -> str:
        return f"Lechuga ({self._variedad} - {self._peso_unidad:.2f}kg)"

    # Contenido CORREGIDO en lechuga.py (Asumo que hereda de Hortaliza)

