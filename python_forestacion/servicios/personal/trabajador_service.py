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

    def trabajar(self, trabajador: Trabajador, fecha: date, util: Herramienta) -> bool:
        """
        Ejecuta las tareas asignadas al trabajador para la fecha dada (US-016).
        Las tareas se ejecutan en orden ID descendente.
        """
        if not self.puede_trabajar(trabajador):
            print(f"[!] {trabajador.get_nombre()} NO puede trabajar: Sin apto medico")
            return False

        print(f"[OK] {trabajador.get_nombre()} trabajando el {fecha}")

        # 1. Obtener y ordenar tareas por ID descendente (US-016)
        tareas_pendientes = [
            t for t in trabajador.get_tareas_asignadas() 
            if t.get_estado() == EstadoTarea.PENDIENTE and t.get_fecha_programada() == fecha
        ]
        
        # Ordenamiento ID descendente (3, 2, 1)
        tareas_pendientes.sort(key=TrabajadorService._obtener_id_tarea, reverse=True) 
        
        # 2. Ejecutar y marcar como completada
        for tarea in tareas_pendientes:
            print(f"      Tarea #{tarea.get_id()}: {tarea.get_nombre()}")
            print(f"      Usando: {util.get_nombre()}")
            tarea.marcar_completada() # Aunque en esta simple simulación no modificamos la lista del trabajador

        return True