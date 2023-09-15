from dash import dcc, html
import pandas as pd

from utils import get_stock_data,get_connection

def fetch_debtToEquity_data(ticker='GOOGL'):

    conn = get_connection()
    balance_sheet = get_stock_data(conn, 'balance_sheet_quarterly', [ticker])

    balance_sheet['debtToEquity'] = balance_sheet['total_current_liabilities']/balance_sheet['total_shareholder_equity']
    balance_sheet = balance_sheet[['symbol', 'fiscal_date_ending', 'debtToEquity']]

    return balance_sheet

def create_debtToEquity_graph():

    debtToEquity = dcc.Graph(
        id='debtToEquity-graph',
        style={'width': '100%'}
    )

    return debtToEquity