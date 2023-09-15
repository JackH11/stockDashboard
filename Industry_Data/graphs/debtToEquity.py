from dash import dcc, html
import pandas as pd

from utils import get_stock_data,get_connection

from plotly.subplots import make_subplots
import plotly.graph_objects as go

def fetch_debtToEquitys_data(ticker='GOOGL'):

    conn = get_connection()
    balance_sheet = get_stock_data(conn, 'balance_sheet_quarterly', [ticker])

    balance_sheet['debtToEquity'] = balance_sheet['total_current_liabilities']/balance_sheet['total_shareholder_equity']
    balance_sheet = balance_sheet[['symbol', 'fiscal_date_ending', 'debtToEquity']]

    return balance_sheet

def create_debtToEquity_graph():


    fig = make_subplots(rows=1, cols=4)
    for i in range(1, 5):
        scatter = go.Scatter(x=[], y=[], mode='markers')
        fig.add_trace(scatter, row=1, col=i)

    fig.update_layout(title='Debt to Equity', showlegend=False)
    fig.update_layout(
        showlegend=False,
        xaxis=dict(title='', showgrid=False, zeroline=False),
        yaxis=dict(title='Debt to Equity', showgrid=False, zeroline=False),
        plot_bgcolor='#1E1E24',
        paper_bgcolor='#1E1E24',
        margin={'l': 50, 'r': 10, 't': 60, 'b': 40}
    )
    figure = dcc.Graph(id='debtToEquity-subplot', style={'width': '100%', 'height': '100%'})
    return figure

    """
    figures = []
    for i in range(1,5):
        figure = dcc.Graph(
            id=f'debtToEquity-graph{i}',
            style={'width': '100%', 'height':'100%'}
        )
        figures.append(figure)

    return figures
    """