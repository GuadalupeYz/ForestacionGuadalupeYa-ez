
from python_forestacion.patrones.singleton.singleton import Singleton
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from typing import Type, Dict, Any

# Esta clase actúa como el Registry (Patrón Singleton + Patrón Registry)
# Mapea el nombre del cultivo a su servicio de lógica concreto
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
            # Nota: El registro se realiza automáticamente al importar los módulos de servicio.
            # print(f"[REGISTRY]: Servicio para '{tipo_cultivo}' registrado.")

    def obtener_servicio(self, tipo_cultivo: str) -> Any:
        """Devuelve la instancia del servicio de cultivo para un tipo dado."""
        tipo_cultivo = tipo_cultivo.lower()
        servicio = self._registro.get(tipo_cultivo)
        if not servicio:
            raise ValueError(f"Servicio no encontrado para el tipo de cultivo: {tipo_cultivo}")
        return servicio

    def mostrar_datos(self, cultivo: Cultivo):
        """
        Resuelve el servicio concreto y ejecuta la lógica de mostrar datos.
        """
        tipo = cultivo._nombre.lower() # Asumimos que _nombre es el tipo
        servicio = self.obtener_servicio(tipo)
        
        # Asume que todos los servicios concretos tienen un método 'mostrar_info'
        print(f"[Info Cultivo {cultivo.get_id()} - {cultivo._nombre}]: Agua: {cultivo.get_agua()}L")
        servicio.mostrar_info(cultivo)

