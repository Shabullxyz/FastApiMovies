
from pydantic import BaseModel, Field
from typing import Optional
from models.movie import Movie as MovieModel



class Movie(BaseModel):
    id : Optional[int] = None
    title: str = Field(default="Nada Creativo", min_length= 3, max_length= 15)
    overview : str = Field(default="Nada Creativo Over", min_length= 5, max_length= 40)
    year : int = Field(default=2022 , le=2022)
    rating : float =Field(ge=1, le=10)
    category : str =Field(min_length=5, max_length=15)
    
    class Config:
        schema_extra = {
        'example':{
            'id': 1,
            'title': 'Mi pelicula',
            'overview': 'Descripcion de la pelicula',
            'year': '2022',
            'rating': 9.8,
            'category': 'Acción'    }}