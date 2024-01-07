import sqlite3

def criar_conexao():
    # Cria ou conecta ao banco de dados
    conn = sqlite3.connect('seu_banco_de_dados.db')
    cursor = conn.cursor()

    # Criação da tabela se não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS gastos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            categoria TEXT,
            quantia INTEGER
        )
    ''')

    conn.commit()
    conn.close()
