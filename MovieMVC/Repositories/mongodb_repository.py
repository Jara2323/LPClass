from movie_repository import MovieRepository

# se aplica la "o" de los principios SOLID: casa repositorio concreto, implementa las operaciones para un store
# especifico 
class MongoDBRepository(MovieRepository):
    
    def get_all(this):
        #return super().get_all()
        return[
        {"title":"Interstellar", "year":2014, "genre":"Ciencia Ficcion", "director":"Christopher Nolan"},
        {"title":"Kimetsu No Yaiba", "year":2025, "genre":"Anime", "director":"Haruo Sotozaki"},
    ]