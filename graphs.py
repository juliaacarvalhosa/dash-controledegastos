import random

import pandas as pd
import numpy as np
import plotly.express as px

from app import palavras_aleatorias, table_data

# Função para criar gráficos
def create_bar_figure(categories, data, colors):
    fig = px.bar(x=categories, y=data, color=colors)
    fig.update_layout(
        title='Gráfico de Renda, Despesa e Gasto',
        xaxis_title='Categorias',
        yaxis_title='Valores ($)',
        plot_bgcolor='black',
        paper_bgcolor='black',
        font_color='white',
        title_font_color='white',
        xaxis=dict(showline=True, showgrid=False, linecolor='white'),
        yaxis=dict(showline=True, showgrid=True, gridcolor='gray', linecolor='white')
    )
    return fig

def create_pie_figure(labels, values):
    fig = px.pie(labels=labels, values=values, names=values)
    fig.update_layout(
        title='Gráfico percentual gasto por categoria',
        paper_bgcolor='black',  # Cor de fundo da área ao redor do gráfico
        font=dict(color='white'),  # Cor do texto
        showlegend=True  # Exibe a legenda
    )
    return fig




