from dash import dcc, html
import pandas as pd

from utils import get_stock_data,get_connection

def fetch_debtToEquitys_data(ticker='GOOGL'):

    conn = get_connection()
    balance_sheet = get_stock_data(conn, 'balance_sheet_quarterly', [ticker])

    balance_sheet['debtToEquity'] = balance_sheet['total_current_liabilities']/balance_sheet['total_shareholder_equity']
    balance_sheet = balance_sheet[['symbol', 'fiscal_date_ending', 'debtToEquity']]

    return balance_sheet

def create_debtToEquity_graph():


    figures = []
    for i in range(1,5):
        figure = dcc.Graph(
            id=f'debtToEquity-graph{i}',
            style={'width': '100%', 'height':'100%'}
        )
        figures.append(figure)

    return figures