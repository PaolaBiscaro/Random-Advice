from fastapi import FastAPI
from database.init_db import create_table
from models.advice import Advice
from services.advice_service import create_advice, get_all_advices


app = FastAPI()
create_table()

@app.get("/")
async def root():
    return{"message": "API Funcionando!"}


@app.get("/view_advices")
def view_advice():
    advices = get_all_advices()
    return advices



@app.post("/register_advice")
def register_advice(advice: Advice):
    id_gerado = create_advice(advice.phrase)
    return {"id": id_gerado,
            "mensagem": "Conselho cadastrado com sucesso."}
    
