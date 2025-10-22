"""
Archivo integrador generado automaticamente
Directorio: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/servicios/cultivos
Fecha: 2025-10-22 10:21:44
Total de archivos integrados: 8
"""

# ================================================================================
# ARCHIVO 1/8: __init__.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/servicios/cultivos/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/8: arbol_service.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/servicios/cultivos/arbol_service.py
# ================================================================================

# Contenido de python_forestacion/servicios/cultivos/arbol_service.py

# Usar importación RELATIVA para módulos dentro del mismo paquete 'cultivos'
from .cultivo_service import CultivoService 

class ArbolService(CultivoService):
    """
    Servicio base para todos los cultivos de tipo árbol (Pino, Olivo).
    """
    
    def __init__(self, estrategia_absorcion):
        super().__init__(estrategia_absorcion)

    def crecer(self, arbol, incremento_metros):
        """Lógica de crecimiento común a todos los árboles."""
        nueva_altura = arbol.get_altura_metros() + incremento_metros
        arbol.set_altura_metros(nueva_altura)
        
    pass

# ================================================================================
# ARCHIVO 3/8: cultivo_service.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/servicios/cultivos/cultivo_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 4/8: cultivo_service_registry.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/servicios/cultivos/cultivo_service_registry.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 5/8: lechuga_service.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/servicios/cultivos/lechuga_service.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 6/8: olivo_service.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/servicios/cultivos/olivo_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 7/8: pino_service.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/servicios/cultivos/pino_service.py
# ================================================================================

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




# ================================================================================
# ARCHIVO 8/8: zanahoria_service.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/servicios/cultivos/zanahoria_service.py
# ================================================================================

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

