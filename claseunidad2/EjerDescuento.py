from abc import ABC, abstractmethod

class Descuento(ABC):
    @abstractmethod
    def aplicar_descuento(self, precio):
        pass 

class DescuentoRegular(Descuento):
    def aplicar_descuento(self, precio):
        print("descuento para cliente regular ")
        return precio * 0.90


class DescuentoPremium(Descuento):
    def aplicar_descuento(self, precio):
        print("descuento para cliente premium ")
        return precio * 0.85


class DescuentoVip(Descuento):
    def aplicar_descuento(self, precio):
        print("descuento para cliente vip ")
        return precio * 0.80

class CarritoDeComprasStrategy:
    def __init__(self, descuento: Descuento):
        self.descuento = descuento

    def set_descuento(self, descuento: Descuento):
        self.descuento = descuento

    def calcular_total(self, precio):
        return self.descuento.aplicar_descuento(precio)

if __name__ == "__main__":
    precio = 1000

    carrito = CarritoDeComprasStrategy(DescuentoRegular())
    print("Total regular:", carrito.calcular_total(precio))

    carrito.set_descuento(DescuentoPremium())
    print("Total premium:", carrito.calcular_total(precio))

    carrito.set_descuento(DescuentoVip())
    print("Total vip:", carrito.calcular_total(precio))