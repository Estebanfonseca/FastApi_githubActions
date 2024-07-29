from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title='Api de prueba para github actions',version='0.0.1',description='probar a subir en github actions')
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def inicio():
    return {'message': 'api de prueba github'}

@app.get('/hola')
def hola():
    return {'message': 'hola mundo api de prueba github'}
