from .cultivo_service import CultivoService
from .cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from typing import Union

class PinoService(CultivoService):
    """Lógica de negocio específica para el cultivo Pino."""
    
    def mostrar_info(self, cultivo: Union[Cultivo, Pino]):
        """Muestra información detallada del Pino."""
        if not isinstance(cultivo, Pino):
             raise TypeError("El cultivo debe ser una instancia de Pino.")

        print(f"  -> Servicio Pino: Variedad={cultivo.get_variedad()}, Altura={cultivo.get_altura():.2f}m.")


# --- REGISTRO DE SERVICIO (CRÍTICO PARA US-009) ---
# Al final del archivo, registra la instancia Singleton del servicio.
CultivoServiceRegistry.get_instance().registrar("Pino", PinoService())