from fastapi import FastAPI
import random
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Meu primeiro EndPoint!"}

# 127.0.0.1:8000/teste
@app.get("/teste")
async def segundoendpoint():
    return {"teste":True, "num_random": random.randint(1,100)}