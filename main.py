from models.jwt_bearer import JWTBearer
from services import movies_service as movies, users_service as users
from models.movie import Movie
from models.user import User
from security.jwt_manager import create_token


from fastapi import Depends, FastAPI, Path, Query, status, HTTPException
from typing import List


app = FastAPI(
    title="Movies API",
    description="This is a practice movies API",
    version="1.0.0"
)

# General

@app.get("/", tags=["Health"], response_model=str, status_code=status.HTTP_200_OK)
def health() -> str:
    return "OK"


# Authentication
@app.post("/login", tags=["Authentication"], response_model=str, status_code=status.HTTP_200_OK)
def login(user: User) -> str:
    return users.login(user)


# Movies


@app.get("/movies", tags=["Movies"], response_model=List[Movie], status_code=status.HTTP_200_OK, dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    return movies.get_movies()


@app.get("/movies/{movie_id}", tags=["Movies"], response_model=Movie, status_code=status.HTTP_200_OK, dependencies=[Depends(JWTBearer())])
def get_movie_by_id(movie_id: int = Path(ge=1)) -> Movie:
    movie = movies.get_movie_by_id(movie_id)
    if not movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
    
    return movie


@app.get("/movies/", tags=["Movies"], response_model=List[Movie], status_code=status.HTTP_200_OK, dependencies=[Depends(JWTBearer())])
def get_movies_by_filter(title: str | None = Query(min_length=5, max_length=50, default=None), director: str | None = Query(min_length=5, max_length=50, default=None), year: int | None = Query(gt=1900, lt=2024, default=None), rating: float | None = Query(ge=0, lt=10, default=None), genre: str | None = Query(min_length=5, max_length=20, default=None)) -> List[Movie]:
    list_of_movies = movies.get_movies_by_filter(title, director, year, rating, genre)
    if not list_of_movies:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
    return list_of_movies


@app.post("/movies", tags=["Movies"], response_model=Movie, status_code=status.HTTP_201_CREATED, dependencies=[Depends(JWTBearer())])
def add_movie(new_movie: Movie) -> Movie:
    added_movie = movies.add_mew_movie(new_movie)
    if not added_movie:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Movie already exists")
    return added_movie


@app.put("/movies/{movie_id}", tags=["Movies"], response_model=Movie, status_code=status.HTTP_200_OK, dependencies=[Depends(JWTBearer())])
def update_movie(new_movie: Movie, movie_id: int = Path(ge=1)) -> Movie:
    updated_movie = movies.update_movie(movie_id, new_movie)
    if not updated_movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
    return update_movie


@app.delete("/movies/{movie_id}", tags=["Movies"], response_model=Movie, status_code=status.HTTP_200_OK, dependencies=[Depends(JWTBearer())])
def delete_movie(movie_id: int = Path(ge=1)) -> Movie:
    deleted_movie = movies.delete_movie(movie_id)
    if not deleted_movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
    return delete_movie
