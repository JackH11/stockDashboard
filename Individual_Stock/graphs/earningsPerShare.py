from dash import dcc, Input, Output
import pandas as pd

from ..utils import get_data,get_connection

tickers = ['BA', 'GE', 'MMM', 'CAT']

pe_data = pd.DataFrame({'symbol': ['BABA', 'GE', 'MMM', 'CAT'],
                        'pe': [18.5, 12.7, 18.3, 20.1]})

# Mock data for the second graph
# Replace this with your actual data
earnings_data = pd.DataFrame({'symbol': ['BA', 'BA', 'GE', 'GE', 'MMM', 'MMM', 'CAT', 'CAT'],
                              'fiscal_date_ending': ['2023-01-01', '2023-02-01', '2023-01-01', '2023-02-01',
                                                     '2023-01-01', '2023-02-01', '2023-01-01', '2023-02-01'],
                              'estimated_eps': [2.0, 1.8, 1.2, 1.5, 2.5, 2.3, 1.9, 2.2],
                              'reported_eps': [1.8, 1.9, 1.0, 1.3, 2.2, 2.0, 1.7, 2.1]})

def fetch_data():
    ticker = 'GOOGL'
    conn = get_connection()
    df = get_data(conn, 'earnings_report_quarterly', [ticker])

    return df


def create_earnings_graph():

    earningsPerShare = dcc.Graph(
        id='earnings-graph',
        style={'width': '100%'}
    )

    return earningsPerShare