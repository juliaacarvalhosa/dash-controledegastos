import random

import numpy as np
import pandas as pd
from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc

from app import categories, data, colors, table_data, palavras_aleatorias
from graphs import create_bar_figure, create_pie_figure

def add_table_row():
    global table_data
    new_row = {'Id': len(table_data) + 1,
               'Categoria': random.choice(palavras_aleatorias),
               'Quantia': np.random.randint(100, 500)}
    # Alteração correta
    table_data = pd.concat([table_data, pd.DataFrame([new_row])], ignore_index=True)

for _ in range(10):
        add_table_row()

def template():
    return html.Div(children=[
        html.H1('Controle de Gastos Pessoal', className='title'),
        html.Div([
            html.Div([
                html.Div([
                    dash_table.DataTable(
                        id='table',
                        columns=[{"name": i, "id": i} for i in table_data.columns],
                        data=table_data.to_dict('records'),
                        style_table={'overflowY': 'auto'},
                        style_cell={'textAlign': 'center'},  # Centraliza o texto nas células
                    )
                ], className='table-container'),
                html.Div([
                    html.Div([
                        html.Label('Renda Mensal Total: ', style={'color': '#ffff'}, className='renda-total'),
                        html.Label('R$2583,96', style={'color': '#ffff'}, className='valor-renda'),
                        html.Br(),
                        html.Label('Total Gastos Mensais: ', style={'color': '#fff'}, className='renda-total'),
                        html.Label('R$1569,63', style={'color': '#fff'}, className='valor-renda'),
                        html.Br(),
                        html.Label('Total Saldo: ', style={'color': '#ffff'}, className='renda-total'),
                        html.Label('R$1014,33', style={'color': '#fff'}, className='valor-renda')
                    ]),
                    dbc.Form([
                        html.Div([
                            html.Label("Inserir Nova Despesa", style={'color': '#ffff'}, className='receita-despesa2'),
                            dcc.Dropdown(id='despesa')
                        ], className='receita-despesa d-flex'),
                        html.Div([
                            html.Label("Quantia", style={'color': '#ffff'}, className='receita-despesa2'),
                            dcc.Input(id='quantia')
                        ], className='receita-despesa'),
                        dbc.Button('Inserir', id='button-inserir', color='primary', className='botao-inserir'),
                        dbc.Form([
                            html.Div([
                                html.Label("Inserir Nova Receita", style={'color': '#ffff'}, className='receita-despesa2'),
                                dcc.Input(id='receita')
                            ], className='receita-despesa'),
                            dbc.Button('Inserir', id='botao-inserir-receita', color='primary', className='botao-inserir')
                        ]),
                        dbc.Form([
                            html.Div([
                                html.Label('Novas Categorias', style={'color': '#ffff'}, className='receita-despesa2'),
                                dcc.Input(id='categoria')
                            ], className='receita-despesa'),
                            dbc.Button('Inserir', id='botao-categoria', color='primary', className='botao-inserir')
                        ])

                    ])
                ], className='table-container', style={'display': 'inline-block'})
            ], className='div-tabela'),
            html.Div([
                dcc.Graph(id='graph1', figure=create_bar_figure(categories, data, colors)),
                dcc.Graph(id='graph2', figure=create_pie_figure(categories, data))
            ], className='graphs-container', style={'width': '50%', 'display': 'inline-block', 'vertical-align': 'top'}),

        ], className='main-container', style={'display': 'flex', 'flex-direction': 'row'}),

    ])
