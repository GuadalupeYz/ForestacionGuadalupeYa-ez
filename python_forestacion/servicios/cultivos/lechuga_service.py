from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.entidades.cultivos.lechuga import Lechuga
# Asumo que tienes el CultivoServiceRegistry
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry 

class LechugaService(CultivoService):
    """Servicio para la gestión y visualización del cultivo de Lechuga."""

    def __init__(self):
        # La lechuga usa absorción constante (ejemplo: 0.5 litros)
        super().__init__(AbsorcionConstanteStrategy(cantidad_constante=0.5))

    # Implementación CRÍTICA del método abstracto
    def mostrar_info(self, cultivo: Lechuga) -> None:
        """Muestra los datos específicos de la lechuga."""
        
        # Llama a la lógica base (si CultivoService tiene implementación, si no, puedes omitirlo)
        super().mostrar_datos(cultivo)
        
        # Muestra los datos únicos de Lechuga
        print(f"  -> Servicio Lechuga: Variedad='{cultivo.get_variedad()}', Peso promedio={cultivo.get_peso_unidad()} kg.")

# Registro del servicio en el Singleton (CRÍTICO para que la importación en main.py funcione)
CultivoServiceRegistry.get_instance().registrar("Lechuga", LechugaService())
