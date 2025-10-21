from datetime import date
from typing import List, Union

from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.entidades.personal.apto_medico import AptoMedico 
from python_forestacion.excepciones.forestacion_exception import ForestacionException

class TrabajadorService:
    """
    Servicio para la gestión de Trabajadores y operaciones de Cosecha (US-014, US-015).
    """

    def asignar_apto_medico(self, trabajador: Trabajador, fecha_vencimiento: date):
        """Asigna un apto médico al trabajador (US-014)."""
        apto = AptoMedico(fecha_vencimiento)
        trabajador.set_apto_medico(apto)
        print(f"Trabajador {trabajador._nombre} habilitado con apto hasta {fecha_vencimiento}.")

    def esta_habilitado(self, trabajador: Trabajador) -> bool:
        """Verifica si el trabajador está habilitado para realizar tareas."""
        apto = trabajador.get_apto_medico()
        if not apto or apto._fecha_vencimiento < date.today():
            raise ForestacionException(
                tipo=None, # Asumiendo que no hay TipoOperacion para Personal
                codigo="TRABAJADOR_NO_HABILITADO", 
                mensaje_usuario=f"El trabajador {trabajador._nombre} no tiene apto médico válido para cosechar."
            )
        return True

    def cosechar(self, trabajador: Trabajador, plantacion: Plantacion, tipo_cultivo: str) -> List[Cultivo]:
        """
        Simula la cosecha de todos los cultivos de un tipo específico (US-015).
        """
        self.esta_habilitado(trabajador) # Verifica US-014
        
        cultivos_cosechados: List[Cultivo] = []
        cultivos_restantes: List[Cultivo] = []
        
        for cultivo in plantacion.get_cultivos():
            if cultivo._nombre.lower() == tipo_cultivo.lower():
                cultivos_cosechados.append(cultivo)
            else:
                cultivos_restantes.append(cultivo)
                
        # Simular que la cosecha es exitosa y los cultivos son removidos
        plantacion._cultivos = cultivos_restantes
        
        print(f"\n[COSECHA]: Trabajador {trabajador._nombre} cosechó {len(cultivos_cosechados)} {tipo_cultivo}(s).")
        return cultivos_cosechados