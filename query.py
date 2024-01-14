import sqlite3 as lite
import pandas as pd

con = lite.connect('dados.db')

#INSERT 
def insert_categoria(nome : str):
    with con:
        cur = con.cursor()
        cur.execute(f'INSERT INTO Categoria (nome) VALUES ("{nome}")'
)

def insert_receita(valor : float, idCategoria : int):
    with con:
        cur = con.cursor()
        cur.execute(f'INSERT INTO Receita (valor, idCategoria) VALUES ("{valor}", "{idCategoria}")')

def insert_gastos(categoria : str, valor : float, idCategoria : int):
    with con:
        cur = con.cursor()
        cur.execute(f'INSERT INTO Gastos (categoria, valor, idCategoria) VALUES ("{categoria}", "{valor}", "{idCategoria}")')
    
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
# SELECT
def select_categoria():
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Categoria")
        categorias = cur.fetchall()
    return pd.DataFrame(categorias, columns=['Id', 'Categoria'])


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


# Inserir Categorias
insert_categoria("Alimentação")
insert_categoria("Transporte")
insert_categoria("Lazer")

# Inserir Receitas
insert_receita(1000.50, 1)  # Valor: 1000.50, Categoria ID: 1
insert_receita(500.75, 2)   # Valor: 500.75, Categoria ID: 2
insert_receita(200.00, 1)   # Valor: 200.00, Categoria ID: 1

# Inserir Gastos
insert_gastos("Restaurante", 50.20, 1)   # Categoria: Restaurante, Valor: 50.20, Categoria ID: 1
insert_gastos("Gasolina", 30.50, 2)      # Categoria: Gasolina, Valor: 30.50, Categoria ID: 2
insert_gastos("Cinema", 20.00, 3)        # Categoria: Cinema, Valor: 20.00, Categoria ID: 3

print('Dados inseridos com sucesso!')
