from typing import List, Optional
from python_forestacion.entidades.personal.tarea import Tarea  # Importar Tarea
from python_forestacion.entidades.personal.apto_medico import AptoMedico  # Importar AptoMedico
import copy  # Necesario para defensive copy (US-014, US-017)

class Trabajador:
    """Representa un trabajador con tareas asignadas y apto médico."""

    def __init__(self, dni: int, nombre: str, tareas: List[Tarea] = None, apto_medico: Optional[AptoMedico] = None):
        self._dni = dni
        self._nombre = nombre
        self._tareas = tareas if tareas is not None else []
        self._apto_medico = apto_medico

    def get_dni(self) -> int:
        return self._dni

    def get_nombre(self) -> str:
        return self._nombre

    def get_tareas_asignadas(self) -> List[Tarea]:
        """Retorna una copia inmutable (defensive copy) de la lista de tareas."""
        return copy.deepcopy(self._tareas)

    def get_tareas(self):
        """Alias de get_tareas_asignadas() para compatibilidad con el servicio."""
        return self.get_tareas_asignadas()

    def get_apto_medico(self) -> Optional[AptoMedico]:
        return self._apto_medico

    def set_apto_medico(self, apto: AptoMedico):
        """Asigna o actualiza el apto médico."""
        self._apto_medico = apto

    def __str__(self):
        estado_apto = "CON apto" if self._apto_medico and self._apto_medico.esta_apto() else "SIN apto"
        return f"{self._nombre} (DNI: {self._dni}) - {estado_apto}"
