from dash import Dash, html, dcc, Input, Output, dash_table
import plotly.express as px
import pandas as pd
import numpy as np
import random 
import string 
import dash_bootstrap_components as dbc


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
# Dados
np.random.seed(69)

data = np.random.randint(100, 500, 3)

categories = ['Renda', 'Saldo', 'Despesas']

colors = ['blue', 'red', 'green']

tamanho_da_palavra = 8
quantidade_de_palavras = 20

palavras_aleatorias = [''.join(random.choice(string.ascii_lowercase) for _ in range(tamanho_da_palavra)) for _ in range(quantidade_de_palavras)]

# Criar dados para a tabela
table_data = pd.DataFrame(columns=['Id', 'Categoria', 'Quantia'])

# Função para adicionar novas linhas à tabela
def add_table_row():
    global table_data
    new_row = {'Id': len(table_data) + 1,
               'Categoria': random.choice(palavras_aleatorias),
               'Quantia': np.random.randint(100, 500)}
    # Alteração correta
    table_data = pd.concat([table_data, pd.DataFrame([new_row])], ignore_index=True)

# Adicionar algumas linhas iniciais
for _ in range(10):
    add_table_row()


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

app.layout = html.Div(children=[
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
                    html.Label('Renda Mensal Total: ', style={'color' : '#ffff'}, className='renda-total'),
                    html.Label('R$2583,96', style={'color' : '#ffff'}, className='valor-renda'),
                    html.Br(),
                    html.Label('Total Gastos Mensais: ', style={'color' : '#fff'}, className='renda-total'),
                    html.Label('R$1569,63', style={'color':'#fff'}, className='valor-renda'),
                    html.Br(),
                    html.Label('Total Saldo: ', style={'color' : '#ffff'}, className='renda-total'),
                    html.Label('R$1014,33', style={'color':'#fff'}, className='valor-renda')
                ]),
               dbc.Form([
                   html.Div([
                   html.Label("Inserir Nova Despesa", style={'color' : '#ffff'}, className='receita-despesa2'),
                   dcc.Dropdown(id='despesa')
               ], className='receita-despesa d-flex'),
               html.Div([
                   html.Label("Quantia", style={'color' : '#ffff'}, className='receita-despesa2'),
                   dcc.Input(id='quantia') 
               ], className='receita-despesa'),
                    dbc.Button('Inserir', id='button-inserir', color='primary', className='botao-inserir'),
                dbc.Form([
                    html.Div([
                    html.Label("Inserir Nova Receita", style={'color' : '#ffff'}, className='receita-despesa2'),
                    dcc.Input(id='receita')
                    ], className='receita-despesa'),
                    dbc.Button('Inserir', id='botao-inserir-receita', color='primary', className='botao-inserir')
                ]),
                dbc.Form([
                    html.Div([
                        html.Label('Novas Categorias', style={'color' : '#ffff'}, className='receita-despesa2'),
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

# Callbacks
@app.callback(
    Output('graph1', 'figure'),  # Elemento a ser atualizado
    Input('graph1', 'clickData')  # Trigger para atualização
)
def update_bar_chart(clickData):
    # Atualiza o gráfico de barras com base no clique (exemplo)
    # Implemente a lógica de filtragem conforme necessário
    return create_bar_figure(categories, data, colors)

# Execução
if __name__ == '__main__':
    app.run_server(debug=True)