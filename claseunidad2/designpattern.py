#esta implementación "naive" reemplaza el método constructor por defecto por un
#método propio de instanciación
class persona():
    def __init__(self, nombre):
        self.nombre=nombre


class naive_singleton():
    _instance_ = None
    #se va a lanzar error cuando se llame, para obligar a llamar al método create_instance
    def __init__(self):
        raise RuntimeError("use create_instance method instead")
    #Se usa este método en vez del inicializador para garantizar que se cree una sola instancia
    #classmethod garantiza que el método sea estático
    #cls se usa aquí como el self
    @classmethod 
    def create_instance(cls):
        #si no existe la instancia, la crea
        if cls._instance_  is None:
            cls._instance_ = cls.__new__(cls)
        #retorna la instancia
        return cls._instance_

#ambos objetos SON la misma instancia de la clase
printer_pool1 = naive_singleton.create_instance()
printer_pool2 = naive_singleton.create_instance()

persona1=persona("Camilo")
persona2=persona("Lina")

print(printer_pool1)
print(printer_pool2)

#Debe mostrar si printer_pool1 y printer_pool2 corresponden a la misma instancia de clase (en este caso, es VERDADERO):
print(f"Son la misma instancia?: {printer_pool1 is printer_pool2}")

#ejercicio: Usar el patron singleton para simular el manejo de sesion de usuario de una plataforma de SW
# con la funcionalidad de autenticacion (login) (simulada) con usuario y contraseña y (logout)

# Factory Method: provee formas de crear objetos en una superclase (interfaz) pero son las subclases las que deciden como crearlos
# Abstract Factory: Permite crear familias de objetos sin definir sus implementaciones concretas 

