import sqlite3 as lite

con = lite.connect('dados.db')

#CRIAÇÃO DAS TABELAS

with con:
    cur=con.cursor()
    cur.execute('CREATE TABLE Categoria(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)')

with con:
    cur = con.cursor()
    cur.execute('CREATE TABLE Receita(id INTEGER PRIMARY KEY AUTOINCREMENT, valor DECIMAL)')

with con:
    cur = con.cursor()
    cur.execute('CREATE TABLE Gastos(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, valor DECIMAL)')