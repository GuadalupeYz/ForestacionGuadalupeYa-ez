"""
Archivo integrador generado automaticamente
Directorio: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/servicios/terrenos
Fecha: 2025-10-22 10:21:44
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/servicios/terrenos/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: plantacion_service.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/servicios/terrenos/plantacion_service.py
# ================================================================================

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
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry

class PlantacionService:
    
    def __init__(self):
        # Es crucial que PlantacionService tenga una referencia a la Registry
        self._cultivo_registry = CultivoServiceRegistry() # O CultivoServiceRegistry.obtener_instancia()

    # CRÍTICO: Implementar el método getter para resolver el error fatal.
    def get_cultivo_service_registry(self) -> CultivoServiceRegistry:
        """Retorna la instancia del Singleton CultivoServiceRegistry."""
        return self._cultivo_registry 
    
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

# ================================================================================
# ARCHIVO 3/4: registro_forestal_service.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/servicios/terrenos/registro_forestal_service.py
# ================================================================================

# Archivo: python_forestacion/servicios/terrenos/registro_forestal_service.py
# ESTE ARCHIVO DEBE CONTENER LA CLASE SERVICIO 'RegistroForestalService'

import pickle
import os
from typing import Dict, Any
import copy
# CRÍTICO: PersistenciaException hereda de Exception, no de ForestacionException, pero la importamos.
# Asumo que TipoOperacion se importa correctamente desde constantes.
from python_forestacion.excepciones.persistencia_exception import PersistenciaException
from python_forestacion.constantes import DIRECTORIO_DATA, EXTENSION_DATA, TipoOperacion # TipoOperacion debe estar aquí
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal

class RegistroForestalService: 
    """
    Servicio para la persistencia de datos (Guardar/Cargar estado) (US-021, US-022).
    También maneja el reporte de datos completo (US-023).
    """

    def __init__(self, nombre_archivo_base: str = "registro_simulacion"):
        self.DATA_DIR = DIRECTORIO_DATA # "data"
        self._nombre_archivo_base = nombre_archivo_base 
        self._ruta_archivo = os.path.join(self.DATA_DIR, f"{self._nombre_archivo_base}{EXTENSION_DATA}")

        if not os.path.exists(self.DATA_DIR):
            os.makedirs(self.DATA_DIR)

    # --- Persistencia (US-021, US-022) ---

    def persistir(self, registro: RegistroForestal):
        """Guarda el objeto RegistroForestal completo usando pickle (US-021)."""
        try:
            with open(self._ruta_archivo, 'wb') as f: 
                pickle.dump(registro, f)
            print(f"[PERSISTENCIA]: Registro de {registro.get_propietario()} persistido exitosamente en {self._ruta_archivo}") 
        except Exception as e:
            # LLAMADA CORREGIDA: Usando la firma de 4 argumentos: (operacion, nombre_archivo, causa_raiz, error_code)
            raise PersistenciaException(
                operacion=TipoOperacion.GUARDADO,  # Usamos GUARDADO
                nombre_archivo=self._ruta_archivo,
                causa_raiz=str(e),
                error_code=PersistenciaException.COD_PERSISTENCIA_IO # Asumo que COD_PERSISTENCIA_IO existe en PersistenciaException
            )

    @staticmethod
    def leer_registro(nombre_archivo_base: str) -> RegistroForestal:
        """Carga el objeto RegistroForestal completo desde disco (US-022). (Método estático)"""
        ruta_archivo = os.path.join(DIRECTORIO_DATA, f"{nombre_archivo_base}{EXTENSION_DATA}")

        if not os.path.exists(ruta_archivo):
            # LLAMADA CORREGIDA: Usando el método factoría para archivos no encontrados
            raise PersistenciaException(
                operacion=TipoOperacion.CARGA, # Usamos CARGA
                nombre_archivo=ruta_archivo,
                causa_raiz="Archivo no encontrado",
                error_code=PersistenciaException.COD_PERSISTENCIA_IO
            )

        try:
            with open(ruta_archivo, 'rb') as f: 
                registro: RegistroForestal = pickle.load(f)

            print(f"[PERSISTENCIA]: Registro de {registro.get_propietario()} recuperado exitosamente desde {ruta_archivo}")
            return registro
        except (IOError, pickle.UnpicklingError, EOFError) as e:
            # LLAMADA CORREGIDA: Usando el método factoría para errores de deserialización
            # Si tienes un método from_deserialization_exception, úsalo:
            if hasattr(PersistenciaException, 'from_deserialization_exception'):
                raise PersistenciaException.from_deserialization_exception(nombre_archivo=ruta_archivo, e=e)
            else:
                # Si no existe, usamos la llamada directa:
                raise PersistenciaException(
                    operacion=TipoOperacion.CARGA, # Usamos CARGA
                    nombre_archivo=ruta_archivo,
                    causa_raiz=f"Corrupción/Vacío. Detalle: {str(e)}",
                    error_code=PersistenciaException.COD_PERSISTENCIA_CORRUPTO
                )

    # --- Reporte (US-023) ---

    def mostrar_datos(self, registro: RegistroForestal):
        """
        Muestra todos los datos de un registro forestal en formato legible (US-023).
        """
        plantacion = registro.get_plantacion()
        
        # ... (el resto del código de mostrar_datos es correcto y no requiere cambios) ...
        
        print("\n" + "=" * 33)
        print("REGISTRO FORESTAL".center(33))
        print("=" * 33)
        print(f"Padron:      {registro.get_id_padron()}")
        print(f"Propietario: {registro.get_propietario()}")
        print(f"Avaluo:      {registro.get_avaluo():.2f}")
        print(f"Domicilio:   {registro.get_tierra().get_domicilio()}")
        print(f"Superficie:  {registro.get_tierra().get_superficie():.2f} m²")
        print(f"Cultivos:    {len(plantacion.get_cultivos())} plantados")
        print(f"Agua Disp.:  {plantacion.get_agua_disponible():.2f} L")
        print(f"Superficie Ocupada: {plantacion.get_superficie_ocupada():.2f} m²")

        # Sección de Cultivos (US-023)
        print("\n" + "-" * 33)
        print("LISTADO DE CULTIVOS".center(33))
        print("-" * 33)
        registry = CultivoServiceRegistry.get_instance()

        for cultivo in plantacion.get_cultivos():
            registry.mostrar_datos_resumidos(cultivo) 
            print("-" * 15) 

        # Sección de Trabajadores (US-023)
        print("\n" + "-" * 33)
        print("PERSONAL ASIGNADO".center(33))
        print("-" * 33)
        for trabajador in plantacion.get_trabajadores():
            print(f"    {trabajador}")

# ================================================================================
# ARCHIVO 4/4: tierra_service.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/servicios/terrenos/tierra_service.py
# ================================================================================

# python_forestacion/servicios/terrenos/tierra_service.py

# --- Importaciones de Entidades (Correcto) ---
from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion

class TierraService:
    """
    Servicio de gestión de la entidad Tierra y la creación de Plantaciones iniciales.
    """

    # CRÍTICO: El método debe estar indentado DENTRO de la clase TierraService
    def crear_tierra_con_plantacion(
        self, 
        id_padron: int, 
        superficie: float, 
        domicilio: str, 
        nombre_plantacion: str, 
        agua_inicial: float 
    ) -> Tierra:
        """
        Crea una instancia de Tierra y le asigna una Plantacion.
        Este método soluciona el error del argumento 'agua_inicial' que salió anteriormente.
        """
        
        # 1. Crear Plantacion (ahora pasándole el agua inicial)
        plantacion = Plantacion(
            id_padron=id_padron,
            domicilio=domicilio,
            superficie=superficie, # La Plantacion toma la superficie de la Tierra
            nombre_plantacion=nombre_plantacion,
            agua_inicial=agua_inicial # Se usa el valor pasado como argumento
        )
        
        # 2. Crear Tierra
        tierra = Tierra(
            id_padron=id_padron,
            superficie=superficie,
            domicilio=domicilio
        )
        
        # 3. Asignar Plantacion a Tierra
        tierra.set_finca(plantacion)

        return tierra

    # Puedes agregar otros métodos aquí si son necesarios
    # def algun_otro_metodo(self, ...):
    #     pass

