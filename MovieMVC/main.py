from Model import *
from MovieMVC.Repositories.movie_repository import *
from MovieMVC.Repositories.mongodb_repository import *

# principio "L": Principio de sustitucion de liskov: puede usarse una subclase en reemplazo de la superclase
# sin afectar el funcionamiento del modulo o del sistema completo

repo: MovieRepository = MongoDBRepository()
lista_todas_peliculas = repo.getAll()
