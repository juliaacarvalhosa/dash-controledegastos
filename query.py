import sqlite3 as lite

con = lite.connect('dados.db')

#INSERT 
def insert_categoria(nome : str):
    query = "INSERT INTO Categoria (nome) VALUES (?)"

    with con,con.cursor() as cur:
        cur.execute(query, (nome))

def insert_receita(valor : float):
    query = "INSERT INTO Receita (valor) VALUES (?)"

    with con,con.cursor() as cur:
        cur.execute(query, (valor))

def insert_gastos(categoria : str, valor : float):
    query = "INSERT INTO Gastos (categoria, valor) VALUES (?, ?)"

    with con,con.cursor() as cur:
        cur.execute(query, (categoria, valor))
    
#DELETE
def delete_receita(id : int):
    query = "DELETE FROM Receita WHERE id = ?"
    
    with con, con.cursor() as cur:
        cur.execute(query, (id,))

def delete_gastos(id : int):
    query = "DELETE FROM Gastos WHERE id = ?"
    
    with con, con.cursor() as cur:
        cur.execute(query, (id,))


#SELECT
def select_categoria():
    query = "SELECT * FROM Categoria"

    with con, con.cursor as cur:
        cur.execute(query)
        categorias = cur.fetchall()

    return categorias

def select_receita():
    query = "SELECT * FROM Receita"

    with con, con.cursor as cur:
        cur.execute(query)
        receitas = cur.fetchall()

    return receitas

def select_gastos():
    query = "SELECT * FROM Gastos"

    with con. con.cursor as cur:
        cur.execute(query)
        gastos = cur.fetchall()
    return gastos

