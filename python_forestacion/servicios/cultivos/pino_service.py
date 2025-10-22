from .cultivo_service import CultivoService
from .cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.constantes import AGUA_INICIAL_PINO, SUPERFICIE_PINO
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy

class PinoService(CultivoService):
    """Lógica de negocio específica para el cultivo Pino."""
    
def mostrar_info(self, cultivo: Pino) -> None:
    super().mostrar_datos(cultivo)
    super().__init__(AbsorcionSeasonalStrategy())
    print(f"  -> Servicio Pino: Variedad={cultivo.get_variedad()}, Altura={cultivo.get_altura_metros()}m.")


