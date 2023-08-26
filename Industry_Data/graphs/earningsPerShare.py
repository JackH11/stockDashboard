from dash import dcc, Input, Output
import pandas as pd

from utils import get_stock_data,get_connection

from plotly.subplots import make_subplots
import plotly.graph_objects as go


def fetch_earnings_data(ticker='GOOGL'):

    conn = get_connection()
    df = get_stock_data(conn, 'earnings_report_quarterly', [ticker])

    return df


def create_earnings_graph():

    # Takes parameters Ticker 1, Ticker 2, Ticker 3, Ticker 4

    fig = make_subplots(rows=1, cols=4)
    for i in range(1,5):
        scatter = go.Scatter(x=[],y=[],mode='markers')
        fig.add_trace(scatter,row=1,col=i)

    fig.update_layout(title='Earnings Per Share',showlegend=False)
    fig.update_layout(
        title=dict(text='Earnings Subplots', x=0.5),
        showlegend=False,
        xaxis=dict(title='', showgrid=False, zeroline=False),
        yaxis=dict(title='EPS', showgrid=False, zeroline=False),
        plot_bgcolor= '#1E1E24',
        paper_bgcolor= '#1E1E24',
        margin={'l': 50, 'r': 10, 't': 60, 'b': 40}
    )
    figure = dcc.Graph(id='earnings-subplot',style={'width': '100%', 'height':'100%'})
    return figure

    """
    figures = []
    for i in range(1,5):
        figure = dcc.Graph(
            id=f'earnings-graph{i}',
            style={'width': '100%', 'height':'100%'}
        )
        figures.append(figure)
    """

    return figures