import sqlite3

con = sqlite3.connect('dados.db')

with con:
    cur = con.cursor()
    cur.execute('CREATE TABLE Categoria(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)')

with con:
    cur = con.cursor()
    cur.execute('CREATE TABLE Receita(id INTEGER PRIMARY KEY AUTOINCREMENT, valor DECIMAL, idCategoria INTEGER, FOREIGN KEY (idCategoria) REFERENCES Categoria(id))')

with con:
    cur = con.cursor()
    cur.execute('CREATE TABLE Gastos(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, valor DECIMAL, idCategoria INTEGER, FOREIGN KEY (idCategoria) REFERENCES Categoria(id))')
