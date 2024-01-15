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

# Removendo colunas indesejadas
columns_to_drop = ['Id_x', 'Id_y', 'IdCategoria', 'Nome']
for col in columns_to_drop:
    if col in table_data.columns:
        table_data.drop(col, axis=1, inplace=True)

# Removendo duplicatas nas colunas 'Categoria' e 'Valor'
table_data.drop_duplicates(subset=['Categoria', 'Valor'], inplace=True)

# Removendo linhas com valores nulos
table_data.dropna(inplace=True)

# Redefinindo o índice para que os IDs sejam sequenciais
table_data.reset_index(drop=True, inplace=True)
table_data.index += 1
table_data.rename(columns={'index': 'Id'}, inplace=True)
table_data['Id'] = table_data.index

print(table_data)