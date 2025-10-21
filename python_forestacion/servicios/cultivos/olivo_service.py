# En python_forestacion/servicios/cultivos/olivo_service.py

from .cultivo_service import CultivoService
from .cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.entidades.cultivos.olivo import Olivo
# Remueve la importación de Cultivo y Union si no se usan directamente en otros métodos
# from python_forestacion.entidades.cultivos.cultivo import Cultivo 
# from typing import Union 

class OlivoService(CultivoService):
    """Lógica de negocio específica para el cultivo Olivo."""
    
    # ÚNICA definición de mostrar_info
    def mostrar_info(self, cultivo: Olivo): # Usamos Olivo directamente para el type hint
        """Muestra información detallada del Olivo."""
        if not isinstance(cultivo, Olivo):
             raise TypeError("El cultivo debe ser una instancia de Olivo.")
        
        # Esta línea ahora debería funcionar si _edad existe en Olivo (por herencia).
        print(f"  -> Servicio Olivo: Aceituna={cultivo.get_tipo_aceituna().value}, Edad={cultivo.get_edad()} años.") 

# --- REGISTRO DE SERVICIO (CRÍTICO PARA US-009) ---
CultivoServiceRegistry.get_instance().registrar("Olivo", OlivoService())