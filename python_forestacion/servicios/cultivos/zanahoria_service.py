from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry # Debe estar para el registro
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy

class ZanahoriaService(CultivoService):
    """Lógica de negocio específica para el cultivo Zanahoria."""
    
    # ✅ CORRECTO: IMPLEMENTAR EL CONSTRUCTOR
    def __init__(self):
        # La Zanahoria usa absorción constante. Esto resuelve el TypeError.
        super().__init__(AbsorcionConstanteStrategy(cantidad_constante=0.3)) 

    # ✅ CORRECTO: IMPLEMENTAR EL MÉTODO ABSTRACTO (mostrar_info o mostrar_datos, debe ser consistente)
    # NOTA: Asumo que el método correcto es 'mostrar_info', como en LechugaService.
    def mostrar_info(self, cultivo: Zanahoria) -> None:
        """Muestra información detallada de la Zanahoria."""
        
        # Debes llamar al método base, usando el nombre que CultivoService espera (mostrar_info_base)
        super().mostrar_info_base(cultivo) # O super().mostrar_info(cultivo)
        
        tipo = "Baby Carrot" if cultivo.es_baby_carrot() else "Común"
        print(f"  -> Servicio Zanahoria: Tipo={tipo}")

# --- REGISTRO DE SERVICIO (CRÍTICO) ---
CultivoServiceRegistry.get_instance().registrar("Zanahoria", ZanahoriaService())