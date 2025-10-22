# Archivo: python_forestacion/entidades/terrenos/registro_forestal.py
# ESTE ARCHIVO DEBE CONTENER LA CLASE ENTIDAD 'RegistroForestal'

from datetime import date
from typing import List, Optional
from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion

class RegistroForestal:
    """
    Representa el registro formal y catastral de una finca y su plantación.
    (US-003)
    """
    def __init__(self, id_padron: int, tierra: Tierra, plantacion: Plantacion, propietario: str, avaluo: float, fecha_registro: date = None):
        self._id_padron = id_padron
        self._tierra = tierra # Composición: Una Tierra
        self._plantacion = plantacion # Composición: Una Plantacion
        self._propietario = propietario
        self._avaluo = avaluo
        self._fecha_registro = fecha_registro if fecha_registro is not None else date.today()

    # --- Getters (US-003) ---
    def get_id_padron(self) -> int:
        return self._id_padron

    def get_tierra(self) -> Tierra:
        return self._tierra

    def get_plantacion(self) -> Plantacion:
        return self._plantacion

    def get_propietario(self) -> str:
        return self._propietario

    def get_avaluo(self) -> float:
        return self._avaluo

    def get_fecha_registro(self) -> date:
        return self._fecha_registro

    def __str__(self):
        return (f"Registro Forestal #{self._id_padron} - Propietario: {self._propietario}\n"
                f"  Plantación: {self._plantacion.get_nombre()} ({len(self._plantacion.get_cultivos())} cultivos)\n"
                f"  Superficie Total: {self._tierra.get_superficie():.2f} m²")