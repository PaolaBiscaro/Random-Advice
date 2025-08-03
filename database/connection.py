import sqlite3
import os
from sqlite3 import Connection
from dotenv import load_dotenv

load_dotenv(dotenv_path='./.env')

database_name = os.getenv('DATABASE_NAME')
print("Nome do banco carregado:", database_name)

def get_connection():
    conn = sqlite3.connect(database_name)
    return conn

