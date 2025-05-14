import sqlite3
from config import DB_PATH

def conectar():
    if not os.path.exists(DB_PATH):
        criar_banco(DB_PATH)
    return sqlite3.connect(DB_PATH)

def criar_banco(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        CPF TEXT NOT NULL,
                        nome_cliente TEXT NOT NULL,
                        telefone TEXT NOT NULL,
                        endereco TEXT NOT NULL)''')
    conn.commit()
    conn.close()
