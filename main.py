from dash import Input, Output
import numpy as np
import pandas as pd

from app import app
from graphs import create_bar_figure
from template import template

from app import df_categorias


app.layout = template()




# Callbacks
@app.callback(
    Output('graph1', 'figure'),  # Elemento a ser atualizado
    Input('graph1', 'clickData')  # Trigger para atualização
)

def update_bar_chart(clickData):
    # Atualiza o gráfico de barras com base no clique (exemplo)
    # Implemente a lógica de filtragem conforme necessário
    return create_bar_figure(df_categorias['Categoria'])
    
if __name__ == '__main__':
    
    app.run_server(debug=True)