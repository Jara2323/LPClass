from abc import ABC, abstractmethod

# define como controlas las operciones de CRUD
class IMovieRepository(ABC):
    
    @abstractmethod
    def get_all(this):
        pass

# Principio "I": Interface Segregation Principle: se separan comportamienetos en varias interfaces  
#en ves de empacarlas en una sola interfaz
# las subclases implementan solo lo que vayan a usar 
class IReadableRepository(ABC):

    @abstractmethod
    def read_all(this):
        pass

class WritableRepository(ABC):

    @abstractmethod
    def write_all(this):
        pass


    @abstractmethod
    def write_all(this):
        pass
    
    
