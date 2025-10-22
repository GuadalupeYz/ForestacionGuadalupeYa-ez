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