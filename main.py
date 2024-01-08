import random

from dash import Input, Output
import numpy as np
import pandas as pd

from app import app, categories, data, colors, table_data, palavras_aleatorias
from graphs import create_bar_figure
from template import template




app.layout = template()




# Callbacks
@app.callback(
    Output('graph1', 'figure'),  # Elemento a ser atualizado
    Input('graph1', 'clickData')  # Trigger para atualização
)

def update_bar_chart(clickData):
    # Atualiza o gráfico de barras com base no clique (exemplo)
    # Implemente a lógica de filtragem conforme necessário
    return create_bar_figure(categories, data, colors)


if __name__ == '__main__':
    
    app.run_server(debug=True)