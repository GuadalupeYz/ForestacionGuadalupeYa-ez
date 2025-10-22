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