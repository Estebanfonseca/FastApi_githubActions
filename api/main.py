from fastapi import FastAPI
from fastapi.middleware import cors

app = FastAPI(title='Api de prueba para github actions',version='0.0.1',description='probar a subir en github actions')

@app.get('/')
def inicio():
    return {'message': 'api de prueba github'}

