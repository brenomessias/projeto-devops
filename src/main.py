import random
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Estudante(BaseModel):
    name: str
    curso: str
    ativo: bool


@app.get("/")
async def root():
    return {"message": "Meu primeiro EndPoint!"}

# 127.0.0.1:8000/teste
@app.get("/teste")
async def segundoendpoint():
    return {"teste":True, "num_random": random.randint(1,100)}

@app.post("/estudantes/cadstro")
async def create_estudante(estudante: Estudante):
    return estudante

@app.put("/estudantes/update/{id_estudante}")
async def update_estudante(id_estudante:int):
    return id_estudante > 0

@app.delete("/estudantes/delete/{id_estudante}")
async def delete_estudante(id_estudante: int):
    return id_estudante > 0