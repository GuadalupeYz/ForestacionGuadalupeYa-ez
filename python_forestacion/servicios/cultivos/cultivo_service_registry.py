from python_forestacion.patrones.singleton.singleton import Singleton
from typing import Any, TYPE_CHECKING
from python_forestacion.entidades.cultivos.cultivo import Cultivo

# CRÍTICO: Importación Diferida (para evitar problemas de ruta/ciclos)
if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion
    from typing import Dict

class CultivoServiceRegistry(Singleton):
    """
    Registro Singleton para los servicios de cultivo concretos (US-009).
    Asegura que solo haya una instancia y centraliza la resolución de servicios.
    """
    def __init__(self):
        # Usamos un flag para garantizar que la inicialización solo ocurra una vez
        if not hasattr(self, '_initialized'):
            self._registro: Dict[str, Any] = {}
            self._initialized = True
            print("[REGISTRY]: CultivoServiceRegistry inicializado.")
    
    def registrar(self, tipo_cultivo: str, servicio_instance: Any):
        """Registra una instancia de servicio concreto (ej: PinoService)."""
        tipo_cultivo = tipo_cultivo.lower()
        if tipo_cultivo not in self._registro:
            self._registro[tipo_cultivo] = servicio_instance
    
    def obtener_servicio(self, tipo_cultivo: str) -> Any:
        """Devuelve la instancia del servicio de cultivo para un tipo dado."""
        tipo_cultivo = tipo_cultivo.lower()
        servicio = self._registro.get(tipo_cultivo)
        if not servicio:
            raise ValueError(f"Servicio no encontrado para el tipo de cultivo: {tipo_cultivo}")
        return servicio
    
    def mostrar_datos(self, plantacion: 'Plantacion'):
        self.mostrar_info(plantacion)
    
    def mostrar_datos_resumidos(self, cultivo):
        """Muestra datos resumidos de un cultivo individual"""
        print(f"    Tipo: {type(cultivo).__name__}")
        print(f"    Superficie: {cultivo.get_superficie():.2f} m²")
        print(f"    Agua: {cultivo.get_agua():.2f} L")  # ← CORREGIDO: get_agua() en lugar de get_agua_disponible()
    
    def mostrar_info(self, plantacion: 'Plantacion'):
        """Muestra información detallada de los cultivos."""
        print("--- REPORTE FINAL DE CULTIVOS EN PLANTACIÓN ---")
        cultivos_a_mostrar = plantacion.get_cultivos()
        for cultivo in cultivos_a_mostrar:
            print(f" [Info Cultivo {cultivo.get_id()}] - {cultivo.get_nombre()}: Agua: {cultivo.get_agua():.2f} L")