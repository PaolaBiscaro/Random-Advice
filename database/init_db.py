from database.connection import get_connection

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS advices(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            phrase TEXT NOT NULL
        )           
    ''')
    conn.commit()
    conn.close()
