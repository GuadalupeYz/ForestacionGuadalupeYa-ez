"""
Archivo integrador generado automaticamente
Directorio: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/entidades/personal
Fecha: 2025-10-22 10:21:44
Total de archivos integrados: 5
"""

# ================================================================================
# ARCHIVO 1/5: __init__.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/entidades/personal/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/5: apto_medico.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/entidades/personal/apto_medico.py
# ================================================================================

# Archivo: python_forestacion/entidades/personal/apto_medico.py
from datetime import date
from typing import Optional

class AptoMedico:
    """Representa el certificado de aptitud de un trabajador."""
    
    def __init__(self, apto: bool, fecha_emision: date, observaciones: Optional[str] = None):
        self._apto = apto
        self._fecha_emision = fecha_emision
        self._observaciones = observaciones or "Sin observaciones"

    def esta_apto(self) -> bool:
        """Retorna True si el trabajador está certificado como apto."""
        # NOTA: En un sistema real se chequearía la fecha de vencimiento (fecha_emision + X años).
        return self._apto

    def get_fecha_emision(self) -> date:
        return self._fecha_emision

    def get_observaciones(self) -> str:
        return self._observaciones

    def __str__(self):
        estado = "APTO" if self._apto else "NO APTO"
        return f"Certificado: {estado} (Emitido: {self._fecha_emision})"

# ================================================================================
# ARCHIVO 3/5: herramienta.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/entidades/personal/herramienta.py
# ================================================================================

class Herramienta:
    """Representa una herramienta de trabajo con ID único y certificación H&S."""
    
    _next_id = 1 # Contador para asignar IDs únicos

    def __init__(self, nombre: str, descripcion: str, certificacion_hs: bool, operativa: bool = True):
        # Asignación de ID único
        self._id = Herramienta._next_id
        Herramienta._next_id += 1
        
        self._nombre = nombre
        self._descripcion = descripcion
        self._operativa = operativa
        self._certificacion_hs = certificacion_hs # Requisito del README: Certificación H&S

    def get_id(self) -> int:
        """Obtiene el ID único de la herramienta."""
        return self._id

    def get_nombre(self) -> str:
        return self._nombre

    def esta_operativa(self) -> bool:
        """Verifica si la herramienta está en condiciones de uso."""
        return self._operativa

    def tiene_certificacion_hs(self) -> bool:
        """Verifica si la herramienta posee la certificación de Salud y Seguridad (H&S)."""
        return self._certificacion_hs

    def set_operativa(self, estado: bool):
        """Cambia el estado operativo de la herramienta (ej. por avería)."""
        self._operativa = estado

    def __str__(self):
        estado = "Operativa" if self._operativa else "En Reparación"
        cert = "Certificada H&S" if self._certificacion_hs else "NO Certificada"
        return f"Herramienta #{self._id}: {self._nombre} ({estado}, {cert})"

# ================================================================================
# ARCHIVO 4/5: tarea.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/entidades/personal/tarea.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 5/5: trabajador.py
# Ruta: /home/guadalupe/Documentos/DiseñoSistemas/Parcial/ForestacionGuadalupeYa-ez/python_forestacion/entidades/personal/trabajador.py
# ================================================================================

# Archivo: python_forestacion/entidades/personal/trabajador.py
from typing import List, Optional
from python_forestacion.entidades.personal.tarea import Tarea # Importar Tarea
from python_forestacion.entidades.personal.apto_medico import AptoMedico # Importar AptoMedico
import copy # Necesario para defensive copy (US-014, US-017)

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

    def get_apto_medico(self) -> Optional[AptoMedico]:
        return self._apto_medico

    def set_apto_medico(self, apto: AptoMedico):
        """Asigna o actualiza el apto médico."""
        self._apto_medico = apto

    def __str__(self):
        estado_apto = "CON apto" if self._apto_medico and self._apto_medico.esta_apto() else "SIN apto"
        return f"{self._nombre} (DNI: {self._dni}) - {estado_apto}"

