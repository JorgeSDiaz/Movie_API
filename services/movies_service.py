from models.movie import Movie


MOVIES_LIST = [
    Movie(id=1, title="The Godfather", director="Francis Ford Coppola", year=1972, rating=9.2, genre="Crime, Drama", description="The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son."),
    Movie(id=2, title="The Shawshank Redemption", director="Frank Darabont", year=1994, rating=9.3, genre="Drama", description="Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency."),
    Movie(id=3, title="The Dark Knight", director="Christopher Nolan", year=2008, rating=9.0, genre="Action, Crime, Drama", description="When the menace known as The Joker emerges, Batman must confront one of the greatest psychological tests of his ability to fight injustice."),
    Movie(id=4, title="Pulp Fiction", director="Quentin Tarantino", year=1994, rating=8.9, genre="Crime, Drama", description="The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption."),
    Movie(id=5, title="Django Unchained", director="Quentin Tarantino", year=2012, rating=8.4, genre="Drama, Western", description="With the help of a German bounty hunter, a freed slave sets out to rescue his wife from a brutal Mississippi plantation owner.")
]


def get_movies():
    global MOVIES_LIST
    return MOVIES_LIST


def get_movie_by_id(movie_id: int):
    movie = list(filter(lambda movie: movie.id == movie_id, get_movies()))
    return len(movie) > 0 and movie[0] or None


def get_movie_by_title(title: str):
    movie = list(filter(lambda movie: movie.title == title, get_movies()))
    return len(movie) > 0 and movie[0] or None


def get_movies_by_filter(title: str = None, director: str = None, year: int = None, rating: float = None, genre: str = None) -> list:
    movies = get_movies()
    if title:
        movies = list(filter(lambda movie: movie.title == title, movies))
    if director:
        movies = list(filter(lambda movie: movie.director == director, movies))
    if year:
        movies = list(filter(lambda movie: movie.year == year, movies))
    if rating:
        movies = list(filter(lambda movie: movie.rating == rating, movies))
    if genre:
        movies = list(filter(lambda movie: movie.genre == genre, movies))
    return movies

def add_mew_movie(new_movie: Movie) -> Movie:
    global MOVIES_LIST
    if get_movie_by_id(new_movie.id) and get_movie_by_title(new_movie.title):
        return None
    MOVIES_LIST.append(new_movie)
    return get_movie_by_title(new_movie.title)


def update_movie(movie_id: int, new_movie: Movie) -> Movie:
    global MOVIES_LIST
    movie = get_movie_by_id(movie_id)
    if not movie:
        return None    
    movie.title = new_movie.title
    movie.director = new_movie.director
    movie.year = new_movie.year
    movie.rating = new_movie.rating
    movie.genre = new_movie.genre
    movie.description = new_movie.description
    return get_movie_by_id(movie_id)

def delete_movie(movie_id: int) -> Movie:
    global MOVIES_LIST
    movie = get_movie_by_id(movie_id)
    if not movie:
        return None
    
    MOVIES_LIST = list(filter(lambda movie: movie.id != movie_id, MOVIES_LIST))
    return movie
