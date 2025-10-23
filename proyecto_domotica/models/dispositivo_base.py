from abc import ABC, abstractmethod
from interfaces.dispositivo_interface import IDispositivo

class DispositivoBase(IDispositivo, ABC):

    def __init__(self, id_dispositivo: int, nombre: str, agente: int):
        self._id = id_dispositivo
        self._nombre = nombre
        self._agente = agente
        self._activo = False

    @property
    def id(self) -> int:
        return self._id

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def agente(self) -> int:
        return self._agente

    @property
    def activo(self) -> bool:
        return self._activo

    @activo.setter
    def activo(self, valor: bool):
        self._activo = valor

    def obtener_info_basica(self) -> str:
        estado = "Activo" if self._activo else "Inactivo"
        return f"{self._nombre} (ID:{self._id}) - Agente {self._agente} - {estado}"

    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass

    @abstractmethod
    def obtener_estado(self) -> str:
        pass

    def obtener_info(self) -> dict:
        return {
            'id': self._id,
            'nombre': self._nombre,
            'agente': self._agente,
            'activo': self._activo
        }
