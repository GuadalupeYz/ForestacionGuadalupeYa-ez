from abc import ABC, abstractmethod
# 2. USAR EL NOMBRE CORRECTO DE LA CLASE: EstrategiaAbsorcion
from python_forestacion.patrones.strategy.absorcion_agua_strategy import EstrategiaAbsorcion 

# 3. Importar las implementaciones de estrategia (para que los hijos puedan inicializarse)
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy

class CultivoService(ABC):
    """Clase base abstracta para todos los servicios de cultivo."""

    # El constructor ahora debe esperar el tipo correcto:
    def __init__(self, estrategia_absorcion: EstrategiaAbsorcion):
        self._estrategia_absorcion = estrategia_absorcion
    
    # CRÍTICO: El método abstracto que todos los hijos deben implementar
    @abstractmethod
    def mostrar_info(self, cultivo) -> None:
        """Muestra información detallada del cultivo."""
        pass
    # En python_forestacion/servicios/cultivos/cultivo_service.py
def regar(self, cultivo):
    """Usa la estrategia para calcular la absorción."""
    # El método absorber_agua DEBE retornar un float.
    agua_a_absorber = self._estrategia_absorcion.absorber_agua(cultivo) 
    # Aquí se hace la lógica de riego y se le suma al cultivo si es necesario.
    # cultivo.set_agua(cultivo.get_agua_actual() + agua_a_absorber) 
    return agua_a_absorber
        
    def mostrar_info_base(self, cultivo):
        print(f"  Cultivo: {cultivo.get_nombre()}, Agua: {cultivo.get_agua_actual()} L")