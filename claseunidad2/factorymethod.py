from abc import ABC, abstractmethod
#factory method 

#producto (clase de objetos) a crear

def ITransporte(ABC):

    @abstractmethod
    def realizar_entrega(self):
        return super().realizar_entrega()

class terrestre_Camion(ITransporte):
    def realizar_entrega(self):
        return super().realizar_entrega()

class terrestre_motocicleta(ITransporte):
    def realizar_entrega(self):
        return super().realizar_entrega()

class Aereo(ITransporte):
    def realizar_entrega(self):
        return super().realizar_entrega()

#Clase creadora - se le delega la creacion a esta clase (tiene el factory method)
class logisticaEntrega(ABC):

    @abstractmethod
    def crear_metodoentrega(self):
        pass
    
    def planificarEntrega(self):
        tipotransporte = self.crear_metodoentrega()
        return tipotransporte.realizar_entrega()
    
#uso de las clases concretas
class entregaTerrestre_Camion(logisticaEntrega):
    def crear_metodoentrega(self):
        return terrestre_Camion()
    
class entregaTerrestre_motocicleta(logisticaEntrega):
    def crear_metodoentrega(self):
        return terrestre_motocicleta()
    
#uso: 

entrega_c = entregaTerrestre_Camion()
print(entrega_c.planificarEntrega())
entrega_m = entregaTerrestre_motocicleta()
