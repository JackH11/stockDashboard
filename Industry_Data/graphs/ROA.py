from dash import dcc, html
import pandas as pd

from utils import get_stock_data,get_connection


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


    figures = []
    for i in range(1, 5):
        figure = dcc.Graph(
            id=f'ROA-graph{i}',
            style={'width': '100%', 'height': '100%'}
        )
        figures.append(figure)

    return figures