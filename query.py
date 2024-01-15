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

#LABEL RENDA TOTAL
def renda_total():
    with con:
        cur = con.cursor()
        cur.execute("SELECT SUM(valor) AS renda_total FROM Receita")
        renda = cur.fetchall()
    return renda

print(renda_total())

def gasto_total():
    with con:
        cur = con.cursor()
        cur.execute("SELECT SUM(valor) AS renda_total FROM Gastos")
        gasto = cur.fetchall()
    return gasto

print(gasto_total())

def saldo_total():
    with con:
        cur = con.cursor()
        cur.execute("SELECT (SELECT SUM(valor) FROM Receita) - (SELECT SUM(valor) FROM Gastos AS Saldo)")
        saldo = cur.fetchall()
    return saldo

print(saldo_total())