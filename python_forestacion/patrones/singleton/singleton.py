class Singleton(object):
    """
    Clase base para implementar el Patrón Singleton (US-009).
    Asegura que solo exista una instancia de la clase.
    """
    _instance = None
    
    # 1. El __new__ maneja la creación la primera vez
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            # Nota: Esto garantiza que la instancia se crea cuando se intenta instanciar
            # Por ejemplo: CultivoServiceRegistry()
        return cls._instance

    @classmethod
    def get_instance(cls, *args, **kwargs):
        """
        Método de acceso estático. Si la instancia no existe, la crea llamando a __new__.
        Esto resuelve el error 'AttributeError: 'NoneType' object has no attribute 'registrar''
        porque garantiza que la instancia exista antes de llamar a 'registrar'.
        """
        if cls._instance is None:
            # Llama a __new__ para forzar la creación si get_instance() es el primer acceso
            cls._instance = cls.__new__(cls, *args, **kwargs)
            # Asegura que __init__ se ejecute si se está creando por primera vez
            if hasattr(cls._instance, '__init__') and not hasattr(cls._instance, '_initialized'):
                cls._instance.__init__(*args, **kwargs)
                
        return cls._instance