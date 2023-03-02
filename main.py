#main Mio
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.login import login_router

app= FastAPI()
app.title = "Mi Api"
app.version = "0.0.2"
app.include_router(login_router)
app.include_router(movie_router)
app.add_middleware(ErrorHandler)

Base.metadata.create_all(bind=engine)

class Config:
    schema_extra = {
        'example':{
            'id': 1,
            'title': 'Mi pelicula',
            'overview': 'Descripcion de la pelicula',
            'year': '2022',
            'rating': 9.8,
            'category': 'Acción'    }}

movies = [{
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    } ]

@app.get('/', tags=["home"])
def message():
    return HTMLResponse('<h1>Hello World</h1>')




