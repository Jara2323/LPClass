from abc import abstractmethod, ABC
#conceptos basicos de oop en python 

#atributos de clase (estaticos) vs atributos de instancia
# de objeto (requiren creacion)
class Estudiante:
    #atributos de clase (estaticos)
    universidad = "Universidad santiago de cali"
    
    #metodo de instancia (crean objetos)
    #recibe como primer parametro, Referencia a la instancia (self)
    def __init__(self, nombre: str, ciudad: str, carrera: str):
        self.nombre = nombre
        self.ciudad = ciudad
        self.carrera = carrera
        self.cursos = []
    #metodo de instancia
    def matricular(self, curso: str):
        self.cursos.append(curso)
        
    @classmethod
    def cambiar_razonsocial(cls, nueva_razonsocial):
        cls.universidad = nueva_razonsocial
    

e1 = Estudiante("Juan", "Cali", "Ingenieria de sistemas")
e2 = Estudiante("Maria", "Bogota", "Medicina")

print(f"El estudiante {e1.nombre} de {e1.universidad} es de la ciudad de {e1.ciudad} y estudia {e1.carrera}")
e1.cambiar_razonsocial("La queridisima universidad de santiago de cali")
print(f"El estudiante {e2.nombre} de {e2.universidad} es de la ciudad de {e2.ciudad} y estudia {e2.carrera}")
print(f"El estudiante {e1.nombre} de {e1.universidad} es de la ciudad de {e1.ciudad} y estudia {e1.carrera}")

#abstraccion y encapsulamiento
#clase abstracta (no se puede instanciar)
class Cuenta(ABC):
    def __init__(self, titular: str, numcuenta: int, saldo: float):
        self.titular = titular
        self.numcuenta = numcuenta
        self.saldo = saldo
        
    #los metodos abstractos deben ser implementados en las clases hijas (subclases)
    @abstractmethod
    def calcular_rendimiento(self):
        pass
    # los metodos no abstractos o concretos pueden ser heredados de las subclases
    # se pueden sobreescribir? 
    def consultar_saldo(self):
        return f"el saldo de la cuenta es {self.saldo}"
    
    def depositar(self, monto: float):
        self.saldo = self.saldo + monto
        
    def retirar(self, monto: float):
        self.saldo = self.saldo - monto
        
class CuentaAhorros(Cuenta):
    porc_rend = 0.1
    def calcular_rendimiento(self):
        #se implementa el metodo abstracto
        self.saldo = self.saldo * (1.0+self.porc_rend)
        #return super().calcular_rendimiento()

class CuentaCorriente(Cuenta):
    cupo_sobregiro = 5000.0
    def calcular_rendimiento(self):
        #se implementa el metodo abstracto
        return super().calcular_rendimiento()
    
    def consultar_saldo(self):
        #se implementa el metodo abstracto
        return super().consultar_saldo()

cuenta1 = CuentaAhorros("Juan", 12345, 1000.0)
cuenta2 = CuentaCorriente("Maria", 67890, 2000.0)

cuenta1.depositar(5000.0)
cuenta2.depositar(1000.0)
print(cuenta1.consultar_saldo())
print(cuenta2.consultar_saldo())

#una interfaz es una clase abstracta que solo tiene metodos abstractos
#(es un contrato) -> las subclases deben implementar todos los metodos
# por otro lado una clase abstracta puede tener una generalizacion
# (ES UNA GENERALIZACION) -> las subclases "extienden"