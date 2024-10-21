
# Projeto de Dashboard Financeiro

Este projeto é um protótipo do [Nibby](https://nibby.fuzzylab.tech), um site desenvolvido para auxiliar no controle de gastos financeiros. Ele apresenta gráficos e tabelas que detalham os gastos por categoria, além de mostrar o percentual de despesas em relação à receita mensal.

## Funcionalidades

- Visualização de receitas e gastos
- Tabelas dinâmicas de dados financeiros
- Gráficos interativos usando o Dash e o Plotly
- Estilização usando Bootstrap para um layout responsivo

## Pré-requisitos

Antes de rodar o projeto, você precisará ter o Python instalado e alguns pacotes. Para instalar as dependências, siga as instruções abaixo:

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Crie um ambiente virtual e ative-o:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Windows use: venv\Scripts\activate
   ```

3. Instale as dependências necessárias:

   ```bash
   pip install -r requirements.txt
   ```

## Como rodar o projeto

Depois de instalar as dependências, você pode rodar o projeto localmente:

```bash
python main.py
```

O servidor será iniciado em `http://127.0.0.1:8050/`. Abra o navegador e visite essa URL para acessar o dashboard.

## Estrutura do Projeto

- `app.py`: Arquivo principal que inicia o servidor Dash e define o layout do dashboard.
- `assets/`: Pasta que contém arquivos estáticos, como estilos CSS.
- `query.py`: Contém as funções de consulta para buscar dados financeiros de receitas, gastos e categorias.
- `requirements.txt`: Lista de dependências necessárias para rodar o projeto.

## Tecnologias Utilizadas

- [Dash](https://plotly.com/dash/) - Framework para construção de aplicações web interativas.
- [Pandas](https://pandas.pydata.org/) - Manipulação e análise de dados.
- [Plotly](https://plotly.com/) - Biblioteca para criação de gráficos interativos.
- [Bootstrap](https://getbootstrap.com/) - Framework para estilização responsiva.








