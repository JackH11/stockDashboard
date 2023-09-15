from dash import dcc, html
import pandas as pd

from utils import get_stock_data,get_connection

from plotly.subplots import make_subplots
import plotly.graph_objects as go


def fetch_ROAs_data(ticker='GOOGL'):

    conn = get_connection()
    cashflow = get_stock_data(conn, 'cashflow_quarterly', [ticker])

    conn = get_connection()
    balance_sheet = get_stock_data(conn, 'balance_sheet_quarterly', [ticker])

    cashflow = pd.merge(cashflow, balance_sheet, on=['symbol', 'fiscal_date_ending'], how='inner')
    cashflow['ROA'] = cashflow['net_income']/cashflow['total_shareholder_equity']
    cashflow = cashflow[['symbol','fiscal_date_ending','ROA']]

    return cashflow

def create_ROAs_graph():

    fig = make_subplots(rows=1, cols=4)
    for i in range(1,5):
        scatter = go.Scatter(x=[],y=[],mode='markers')
        fig.add_trace(scatter,row=1,col=i)

    fig.update_layout(title='Return on Assets',showlegend=False)
    fig.update_layout(
        showlegend=False,
        xaxis=dict(title='', showgrid=False, zeroline=False),
        yaxis=dict(title='EPS', showgrid=False, zeroline=False),
        plot_bgcolor= '#1E1E24',
        paper_bgcolor= '#1E1E24',
        margin={'l': 50, 'r': 10, 't': 60, 'b': 40}
    )
    figure = dcc.Graph(id='roa-subplot',style={'width': '100%', 'height':'100%'})
    return figure


    """
    figures = []
    for i in range(1, 5):
        figure = dcc.Graph(
            id=f'ROA-graph{i}',
            style={'width': '100%', 'height': '100%'}
        )
        figures.append(figure)
    """