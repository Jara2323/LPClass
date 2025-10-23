from abc import ABC, abstractmethod

# Define cómo controlar las operaciones CRUD
class IVehicleRepository(ABC):

    @abstractmethod
    def get_all(this):
        pass


# Principio "I": Interface Segregation Principle
class IReadableRepository(ABC):

    @abstractmethod
    def read_all(this):
        pass


class IWritableRepository(ABC):

    @abstractmethod
    def write_all(this):
        pass

