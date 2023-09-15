from dash import dcc, html
import pandas as pd

from utils import get_stock_data,get_connection


def fetch_PE_data(ticker='GOOGL'):

    conn = get_connection()
    all_eps = get_stock_data(conn, 'earnings_report_quarterly', [ticker])
    all_eps['fiscal_date_ending'] = pd.to_datetime(all_eps['fiscal_date_ending'])


    conn = get_connection()
    all_stocks = get_stock_data(conn, 'stock_history_daily', [ticker])
    all_stocks['etimestamp'] = pd.to_datetime(all_stocks['etimestamp'])

    all_stocks = pd.merge(all_stocks, all_eps, left_on=['symbol', 'etimestamp'],right_on=['symbol', 'fiscal_date_ending'], how='inner')
    all_stocks['PE'] = all_stocks['eclose'] / all_stocks['reported_eps']
    all_stocks = all_stocks[['symbol', 'fiscal_date_ending', 'PE']]


    return all_stocks


def create_PE_graph():
    earningsPerShare = dcc.Graph(
        id='PE-graph',
        style={'width': '100%'}
    )

    return earningsPerShare