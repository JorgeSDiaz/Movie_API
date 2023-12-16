from pydantic import BaseModel, Field

class User(BaseModel):
    email: str = Field(min_length=15, max_length=50)
    password: str = Field(min_length=8, max_length=50)
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "email": "admin@gmail.com",
                "password": "admin123"
                }
            }
        }

user_admin = User(
    email="admin@gmail.com",
    password="admin123"
)