from abc import ABC, abstractmethod

class Trabajador(ABC):
    def __init__(self, apodo: str, codigo: int):  
        self.apodo = apodo
        self.codigo = codigo

    @abstractmethod
    def obtener_pago(self):
        pass

class TrabajadorFijo(Trabajador):
    def __init__(self, apodo: str, codigo: int, sueldo_base: float):  
        super().__init__(apodo, codigo)
        self.sueldo_base = sueldo_base

    def obtener_pago(self):
        return self.sueldo_base

class TrabajadorTiempoMedio(Trabajador):
    def __init__(self, apodo: str, codigo: int, horas_realizadas: float, valor_hora: float):  
        super().__init__(apodo, codigo)
        self.horas_realizadas = horas_realizadas
        self.valor_hora = valor_hora

    def obtener_pago(self):
        return self.horas_realizadas * self.valor_hora

class TrabajadorPrestadorServicio(Trabajador):
    def __init__(self, apodo: str, codigo: int, pago_acordado: float):
        super().__init__(apodo, codigo)
        self.pago_acordado = pago_acordado

    def obtener_pago(self):
        return self.pago_acordado

# Ejemplo de uso:
if __name__ == "__main__": 
    persona1 = TrabajadorFijo("Luna", 101, 32000)
    persona2 = TrabajadorTiempoMedio("Rafa", 100, 40, 45)
    persona3 = TrabajadorPrestadorServicio("Tania", 303, 5000)

    print(f"{persona1.apodo} recibirá: ${persona1.obtener_pago()}")
    print(f"{persona2.apodo} recibirá: ${persona2.obtener_pago()}")
    print(f"{persona3.apodo} recibirá: ${persona3.obtener_pago()}")