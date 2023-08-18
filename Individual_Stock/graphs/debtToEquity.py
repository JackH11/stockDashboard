from dash import dcc, html
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


debtToEquity = dcc.Graph(
    id='debtToEquity-graph',
    figure={
        'data': [
                    {'x': earnings_data[earnings_data['symbol'] == ticker]['fiscal_date_ending'],
                     'y': earnings_data[earnings_data['symbol'] == ticker]['estimated_eps'],
                     'mode': 'markers', 'name': f'Estimated EPS - {ticker}'}
                    for ticker in tickers
                ] + [
                    {'x': earnings_data[earnings_data['symbol'] == ticker]['fiscal_date_ending'],
                     'y': earnings_data[earnings_data['symbol'] == ticker]['reported_eps'],
                     'mode': 'markers', 'name': f'Actual EPS - {ticker}'}
                    for ticker in tickers
                ],
        'layout': {
            'title': 'Debt to Equity',
            'xaxis': {
                'title': 'Fiscal Date Ending',
            },
            'yaxis': {
                'title': 'EPS',
            },
            'grid': {
                'rows': len(tickers) // 2 + 1,
                'columns': 2,
                'pattern': 'independent',
            },
        }
    },
    style={'width':'100%'}
)

def fetch_debtToEquity_data():

    ticker = 'GOOGL'

    conn = get_connection()
    balance_sheet = get_data(conn, 'balance_sheet_quarterly', [ticker])

    balance_sheet['debtToEquity'] = balance_sheet['total_current_liabilities']/balance_sheet['total_shareholder_equity']
    balance_sheet = balance_sheet[['symbol', 'fiscal_date_ending', 'debtToEquity']]

    return balance_sheet

def create_debtToEquity_graph():

    debtToEquity = dcc.Graph(
        id='debtToEquity-graph',
        style={'width': '100%'}
    )

    return debtToEquity