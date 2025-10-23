from Model.movie  import Movie
from View.MovieView import MovieView
from Repositories.movie_repository import IMovieRepository

class MovieController: 
    
    def __init__(this, repository: IMovieRepository, view: MovieView):
        this.repo = repository
        this.view = view

# Implementacion de una funcion de crud que seria llamada desde la vista o 
# o la reportaria ala vista

def list_all_movies(this):
    moviesData = this.repo.get_all()
    #visualiza la informacion atravez del view
    this.view.showMovies(moviesData)
