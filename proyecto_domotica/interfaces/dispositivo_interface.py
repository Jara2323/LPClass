from abc import ABC, abstractmethod

class IDispositivo(ABC):

    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass

    @abstractmethod
    def obtener_estado(self) -> str:
        pass

    @abstractmethod
    def obtener_info(self) -> dict:
        pass
