from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.entidades.cultivos.cultivo import Cultivo
# Asumimos que esta ruta es correcta (Patrón Factory)
from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory 
# Asumimos que estas excepciones y constantes existen
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.constantes import AGUA_MINIMA_RIEGOS
from typing import List

# Implementación CORREGIDA del método plantar en PlantacionService
from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException

class PlantacionService:
    # ... (Otros métodos) ...
    
    def plantar(self, plantacion: Plantacion, tipo_cultivo: str, cantidad: int, **kwargs):
        """
        Planta una cantidad de cultivos de un tipo específico (US-006).
        """
        
        factory = CultivoFactory()
        superficie_requerida = factory.calcular_superficie(tipo_cultivo, cantidad)
        
        tierra = plantacion.get_tierra()
        
        # OBTENER LA SUPERFICIE DISPONIBLE REAL
        # Asumo que la superficie total de la Tierra está en el atributo _superficie
        superficie_total = tierra._superficie 
        
        # Obtener la superficie ya ocupada por otros cultivos
        superficie_ocupada = sum(c._superficie for c in plantacion.get_cultivos())
        
        # Superficie que realmente queda libre
        superficie_disponible = superficie_total - superficie_ocupada
        
        # 3. Comprobar la disponibilidad (US-004)
        if superficie_requerida > superficie_disponible: 
            raise SuperficieInsuficienteException(
                tipo_cultivo=tipo_cultivo, 
                requerida=superficie_requerida, 
                disponible=superficie_disponible
            )
            
        # 4. Crear los cultivos y agregarlos a la plantación
        for _ in range(cantidad):
            cultivo = factory.crear_cultivo(tipo_cultivo, **kwargs)
            plantacion.add_cultivo(cultivo)
            
        print(f"[PLANTACIÓN]: {cantidad} {tipo_cultivo}(s) plantados. Superficie disponible restante: {superficie_disponible - superficie_requerida:.2f} m².")

class PlantacionService:
    """Servicio para la gestión de Plantaciones y Cultivos (US-002, US-004, US-008)."""

    def _get_superficie_ocupada(self, plantacion: Plantacion) -> float:
        """Calcula la superficie total ocupada por los cultivos."""
        return sum(c.get_superficie() for c in plantacion.get_cultivos())

    def plantar(self, plantacion: Plantacion, tipo_cultivo: str, cantidad: int, **kwargs) -> List[Cultivo]:
        """
        Planta uno o varios cultivos verificando la superficie disponible (US-004).
        """
        cultivos_plantados: List[Cultivo] = []
        superficie_ocupada = self._get_superficie_ocupada(plantacion)
        superficie_disponible = plantacion.get_superficie_maxima() - superficie_ocupada
        
        # Crear un cultivo de prueba para obtener su superficie requerida
        cultivo_base = CultivoFactory.crear_cultivo(tipo_cultivo, **kwargs)
        sup_requerida_total = cultivo_base.get_superficie() * cantidad
        
        if sup_requerida_total > superficie_disponible:
            raise SuperficieInsuficienteException(
                tipo_cultivo, sup_requerida_total, superficie_disponible
            )
            
        for i in range(cantidad):
            # Crea la instancia real con el Factory
            nuevo_cultivo = CultivoFactory.crear_cultivo(tipo_cultivo, **kwargs)
            nuevo_cultivo.set_id(len(plantacion.get_cultivos()) + 1)
            plantacion._cultivos.append(nuevo_cultivo)
            cultivos_plantados.append(nuevo_cultivo)
            
        print(f"Plantados {cantidad} {tipo_cultivo}(s) en '{plantacion._nombre}'. Superficie total ocupada: {self._get_superficie_ocupada(plantacion):.2f} m².")
        return cultivos_plantados

    def regar(self, plantacion: Plantacion):
        """
        Simula la absorción de agua por todos los cultivos y consume agua de la plantación (US-008).
        """
        agua_disponible = plantacion.get_agua_disponible()
        
        if agua_disponible < AGUA_MINIMA_RIEGOS:
            raise AguaAgotadaException(agua_disponible)
            
        agua_consumida_total = 0
        
        for cultivo in plantacion.get_cultivos():
            agua_antes = cultivo.get_agua()
            
            # Ejecución del Patrón Strategy (US-008)
            cultivo.get_estrategia().absorber_agua(cultivo) 
            
            agua_despues = cultivo.get_agua()
            agua_consumida = agua_despues - agua_antes
            agua_consumida_total += agua_consumida
            
        # Consumir el agua del tanque de la Plantación
        plantacion.set_agua_disponible(plantacion.get_agua_disponible() - agua_consumida_total)
        
        print(f"Riego completado en '{plantacion._nombre}'. Consumo total: {agua_consumida_total} L. Agua restante: {plantacion.get_agua_disponible()} L.")