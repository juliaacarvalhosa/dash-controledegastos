from dash import Dash
import pandas as pd
import dash_bootstrap_components as dbc
import numpy as np

from query import select_receita, select_categoria, select_gastos

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


data = np.random.randint(100, 500, 3)

categories = ['Renda', 'Saldo', 'Despesas']

colors = ['blue', 'red', 'green']


categorias = select_categoria()
receitas = select_receita()
gastos = select_gastos()

df_categorias = pd.DataFrame(categorias, columns=['Id', 'Nome'])
df_receitas = pd.DataFrame(receitas, columns=['Id', 'Valor', 'IdCategoria'])
df_gastos = pd.DataFrame(gastos, columns=['Id', 'Categoria', 'Valor', 'IdCategoria'])


table_data = pd.merge(df_categorias, df_gastos, left_on='Id', right_on='IdCategoria', how='outer')

print(table_data)