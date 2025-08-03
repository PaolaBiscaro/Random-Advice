#Manipulação do banco de dados (CRUD)
from database.connection import get_connection


#cadastra um conselho
def create_advice(phrase: str):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO advices (phrase) VALUES (?)", (phrase,))
    
    conn.commit()
    advice_id = cursor.lastrowid
    conn.close()
    
    return advice_id


#Lista todos os conselhos
def get_all_advices():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, phrase FROM advices")
    
    rows_advices = cursor.fetchall()
    
    conn.close()
    
    advices = []
    for row in rows_advices:
        advices.append({"id": row[0], "phrase": row[1]})
        
    return advices