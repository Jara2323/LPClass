from controller.MovieController import MovieController
from View.MovieView import MovieView
from Repositories.mongodb_repository import MongoDBRepository

if __name__ == "__main__":
    repo = MongoDBRepository()
    view = MovieView()
    controller = MovieController(repo, view)
    controller.list_all_movies()