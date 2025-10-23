class MovieView:
    
    def showMovies(this, movies):
        print("Esta es la lista de todas las peliculas en la BD")
        for m in movies:
            print(f"Titulo: {m.title}, Año: {m.year}, Genero: {m.genre}, Director: {m.director}")