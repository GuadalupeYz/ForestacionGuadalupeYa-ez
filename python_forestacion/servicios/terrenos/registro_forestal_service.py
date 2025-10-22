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