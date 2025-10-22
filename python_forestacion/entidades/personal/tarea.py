from datetime import date
from enum import Enum
from typing import Optional

class EstadoTarea(Enum):
    PENDIENTE = "Pendiente"
    COMPLETADA = "Completada"

class Tarea:
    """Representa una labor asignada con estado y fecha programada, usando solo PENDIENTE/COMPLETADA."""
    
    _next_id = 1 # Para asignacion de ID unico (para orden descendente de ejecucion)

    def __init__(self, nombre: str, descripcion: str, fecha_programada: date, herramienta_requerida: Optional[str] = None, estado: EstadoTarea = EstadoTarea.PENDIENTE):
        self._id = Tarea._next_id
        Tarea._next_id += 1
        self._nombre = nombre
        self._descripcion = descripcion
        self._fecha_programada = fecha_programada
        self._estado = estado
        self._herramienta_requerida = herramienta_requerida # Opcional: para enlazar con Herramienta

    def get_id(self) -> int:
        """ID único de la tarea para la ejecución ordenada (descendente por ID)."""
        return self._id

    def get_nombre(self) -> str:
        return self._nombre
    
    def get_estado(self) -> EstadoTarea:
        """Estado de tareas (pendiente/completada)."""
        return self._estado

    def get_fecha_programada(self) -> date:
        return self._fecha_programada

    def marcar_completada(self):
        """Cambia el estado de la tarea a COMPLETADA."""
        self._estado = EstadoTarea.COMPLETADA
        
    def __str__(self):
        return f"Tarea #{self._id}: {self._nombre} (Estado: {self._estado.value}, Fecha: {self._fecha_programada})"