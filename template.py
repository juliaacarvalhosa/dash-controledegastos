import random

import numpy as np
import pandas as pd
from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc

from app import categories, data, colors, table_data
from graphs import create_bar_figure, create_pie_figure


def template():
    return html.Div(children=[
        html.H1('Controle de Gastos Pessoal', className='title'),
        
        #Div Geral
        html.Div([
            
            #Valores totais digitais
            html.Div([
                html.Div([
                    html.Label('Renda Mensal Total: ', style={'color': '#ffff'}, className='renda-total'),
                    html.Label('R$ 2583,96', style={'color': '#ffff'}, className='valor-renda'),
                    html.Br(),
                    html.Label('Total Gastos Mensais: ', style={'color': '#fff'}, className='renda-total'),
                    html.Label('R$ 1569,63', style={'color': '#fff'}, className='valor-renda'),
                    html.Br(),
                    html.Label('Total Saldo: ', style={'color': '#ffff'}, className='renda-total'),
                    html.Label('R$ 1014,33', style={'color': '#fff'}, className='valor-renda')
                    ]),
                ], className='table-container-value'),
            html.Div([
                html.Div([
                #Grafico de Barra de Sabão
                dcc.Graph(id='graph1', figure=create_bar_figure(categories, data, colors)),
                ], className='graphs-bar'),
                html.Div([
                #Grafico de Pizza
                dcc.Graph(id='graph2', figure=create_pie_figure(categories, data))
                ], className='graphs-pizza'),
            ], className='graphs-container'),
            
            #Tabela
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
            #Inserção
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
                    ], className='receita-geral'),
                ], className='div-tabela'),
        ], className='main-container'),
    ])
