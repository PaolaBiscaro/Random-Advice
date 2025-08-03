from fastapi import FastAPI
from database.init_db import create_table

app = FastAPI()
create_table()

@app.get("/")
async def root():
    return{"message": "API Funcionando!"}