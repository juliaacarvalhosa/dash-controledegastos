import sqlite3 as lite

con = lite.connect('dados.db')

#INSERT 
def insert_categoria(nome : str):
    with con:
        cur = con.cursor()
        cur.execute(f'INSERT INTO Categoria (nome) VALUES ("{nome}")'
)

def insert_receita(valor : float):
    with con:
        cur = con.cursor()
        cur.execute(f'INSERT INTO Receita (valor) VALUES ("{valor}")')

def insert_gastos(categoria : str, valor : float):
    with con:
        cur = con.cursor()
        cur.execute(f'INSERT INTO Gastos (categoria, valor) VALUES ("{categoria}", "{valor}")')
    
#DELETE
def delete_receita(id : int):
   with con:
        cur = con.cursor()
        cur.execute(f'DELETE FROM Receita WHERE id = ("{id}")')

def delete_gastos(id : int):
    with con:
        cur = con.cursor()
        cur.execute(f'DELETE FROM Gastos WHERE id = ("{id}")')


#SELECT
def select_categoria():
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Categoria")
        categorias = cur.fetchall()

    return categorias

def select_receita():
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Receita")
        receitas = cur.fetchall()

    return receitas

def select_gastos():
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Gastos")
        gastos = cur.fetchall()
    return gastos


print(select_categoria())
print(select_gastos())
print(select_receita())
