from dash import Dash
import pandas as pd
import numpy as np
import random 
import string 
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

np.random.seed(69)

data = np.random.randint(100, 500, 3)

categories = ['Renda', 'Saldo', 'Despesas']

colors = ['blue', 'red', 'green']

tamanho_da_palavra = 8
quantidade_de_palavras = 20

palavras_aleatorias = [''.join(random.choice(string.ascii_lowercase) for _ in range(tamanho_da_palavra)) for _ in range(quantidade_de_palavras)]

table_data = pd.DataFrame(columns=['Id', 'Categoria', 'Quantia'])