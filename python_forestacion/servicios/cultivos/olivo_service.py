from .cultivo_service import CultivoService
from .cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.entidades.cultivos.olivo import Olivo
# Importamos la estrategia correcta para Olivos (árboles)
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy

class OlivoService(CultivoService):
    """Lógica de negocio específica para el cultivo Olivo."""
    
    # CRÍTICO: IMPLEMENTACIÓN DEL CONSTRUCTOR FALTANTE
    def __init__(self):
        # Los Olivos, como árboles, usan la estrategia estacional.
        # Esto resuelve el TypeError que viste en la última traza.
        super().__init__(AbsorcionSeasonalStrategy())
    
    # ÚNICA definición de mostrar_info
    def mostrar_info(self, cultivo: Olivo):
        """Muestra información detallada del Olivo."""
        if not isinstance(cultivo, Olivo):
             raise TypeError("El cultivo debe ser una instancia de Olivo.")
        
        # Esta línea causará un AttributeError si get_edad() no está en Arbol.py
        print(f"  -> Servicio Olivo: Aceituna={cultivo.get_tipo_aceituna().value}, Edad={cultivo.get_edad()} años.") 

# --- REGISTRO DE SERVICIO (CRÍTICO PARA US-009) ---
# Esto ahora llamará al __init__ corregido.
CultivoServiceRegistry.get_instance().registrar("Olivo", OlivoService())