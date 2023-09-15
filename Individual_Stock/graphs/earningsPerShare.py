from dash import dcc, Input, Output
import pandas as pd

from utils import get_stock_data,get_connection


def fetch_data(ticker='GOOGL'):

    conn = get_connection()
    df = get_stock_data(conn, 'earnings_report_quarterly', [ticker])

    return df


def create_earnings_graph():

    earningsPerShare = dcc.Graph(
        id='earnings-graph',
        style={'width': '100%'}
    )

    return earningsPerShare