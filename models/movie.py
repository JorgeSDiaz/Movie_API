from pydantic import BaseModel, Field
from typing import Optional

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=50)
    director: str = Field(min_length=5, max_length=50)
    year: int = Field(gt=1900, lt=2024)
    rating: float = Field(gt=0, lt=10)
    genre: str = Field(min_length=5, max_length=20)
    description: str = Field(min_length=5, max_length=200)
    
    model_config = {
        "json_schema_extra": {
            "example": 
                {
                    "id": 10,
                    "title": "Movie Title",
                    "director": "Movie Director",
                    "year": 1910,
                    "rating": 0.1,
                    "genre": "Movie Genre",
                    "description": "Movie Description"
                }
        }
    }
