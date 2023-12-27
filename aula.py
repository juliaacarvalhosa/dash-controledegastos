# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_excel("Vendas.xlsx")


# CRIANDO O GRÁFICO
fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
opcoes = list(df['ID Loja'].unique())
opcoes.append('Todas')


app.layout = html.Div(children=[
    html.H1(children='Faturamento das Lojas'),
    html.H2(children='Gráfico com o faturamento de todos os produtos separados por loja'),

    html.Div(children='''
        Obs: Esse gráfico mostra a quantidade de produtos vendidos, não o faturamento!
    '''),
    
    dcc.Dropdown(opcoes, value ='Todas', id='Lista lojas'),

    dcc.Graph(
        id='gráfico quantidade de vendas',
        figure=fig #gráfico
    )
])


@app.callback(
    Output('gráfico quantidade de vendas', 'figure'), #quem vai ser editado
    Input('Lista lojas', 'value') #quem vai editar 
)

def update_output(value): #recebe o valor do input
    if value == 'Todas':
        fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    else:
        tabela_filtrada = df.loc[df['ID Loja']== value, :]
        fig = px.bar(tabela_filtrada, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    return fig #retorna o valor que eu quero para o output

#coloca o site no ar
if __name__ == '__main__':
    app.run(debug=True)

#Anotações
#DCC - dash core components