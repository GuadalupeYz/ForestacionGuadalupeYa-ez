"""
Archivo integrador generado automaticamente
Directorio: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/servicios/personal
Fecha: 2025-10-22 12:40:53
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/servicios/personal/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: trabajador_service.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/servicios/personal/trabajador_service.py
# ================================================================================

# Archivo: python_forestacion/servicios/personal/trabajador_service.py
from typing import List
from datetime import date
from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.entidades.personal.apto_medico import AptoMedico
from python_forestacion.entidades.personal.herramienta import Herramienta
from python_forestacion.entidades.personal.tarea import EstadoTarea

class TrabajadorService:
    """Servicio para la gestión de trabajadores, tareas y aptitud médica."""

    def asignar_apto_medico(self, trabajador: Trabajador, apto: bool, fecha_emision: date, observaciones: str = None):
        """Asigna un AptoMedico al trabajador (US-015)."""
        apto_medico = AptoMedico(apto, fecha_emision, observaciones)
        trabajador.set_apto_medico(apto_medico)
        return apto_medico

    def puede_trabajar(self, trabajador: Trabajador) -> bool:
        """Verifica si el trabajador tiene apto médico válido (US-016)."""
        apto = trabajador.get_apto_medico()
        return apto is not None and apto.esta_apto()

    @staticmethod
    def _obtener_id_tarea(tarea):
        """Método estático para el ordenamiento de tareas (US-016)."""
        return tarea.get_id()

    def trabajar(self, trabajador, fecha, util):
    #Simula que un trabajador realiza sus tareas si cuenta con apto médico.
    #Caso contrario, se muestra un mensaje de advertencia y no ejecuta tareas.
    
     apto = trabajador.get_apto_medico()
     if not apto or not apto.esta_apto():
        print(f"[!] {trabajador.get_nombre()} NO puede trabajar: Sin apto medico")
        return False

     print(f"[OK] {trabajador.get_nombre()} trabajando el {fecha}")
     tareas = sorted(trabajador.get_tareas(), key=lambda t: t.get_id(), reverse=True)
     for tarea in tareas:
         print(f"      Tarea #{tarea.get_id()}: {tarea.get_nombre()}")
         print(f"      Usando: {util.get_nombre()}")
     return True



