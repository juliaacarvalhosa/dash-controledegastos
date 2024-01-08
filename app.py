from dash import Dash
import pandas as pd
import numpy as np
import random 
import string 
import dash_bootstrap_components as dbc

from query import select_receita, select_categoria


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

np.random.seed(69)

data = np.random.randint(100, 500, 3)

categories = ['Renda', 'Saldo', 'Despesas']

colors = ['blue', 'red', 'green']

tamanho_da_palavra = 8
quantidade_de_palavras = 20

palavras_aleatorias = [''.join(random.choice(string.ascii_lowercase) for _ in range(tamanho_da_palavra)) for _ in range(quantidade_de_palavras)]

categorias = select_categoria()
receitas = select_receita()

df_categorias = pd.DataFrame(categorias, columns=['Id', 'Categoria'])
df_receitas = pd.DataFrame(receitas, columns=['Id', 'Receita'])


table_data = pd.merge(df_categorias, df_receitas, on='Id', how='outer')

print(table_data)


