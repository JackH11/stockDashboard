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


ROA = dcc.Graph(
    id='ROA-graph',
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
            'title': 'ROA',
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


def fetch_ROA_data():
    ticker = 'GOOGL'
    conn = get_connection()
    cashflow = get_data(conn, 'cashflow_quarterly', [ticker])

    conn = get_connection()
    balance_sheet = get_data(conn, 'balance_sheet_quarterly', [ticker])

    cashflow = pd.merge(cashflow, balance_sheet, on=['symbol', 'fiscal_date_ending'], how='inner')
    cashflow['ROA'] = cashflow['net_income']/cashflow['total_shareholder_equity']
    cashflow = cashflow[['symbol','fiscal_date_ending','ROA']]

    return cashflow

def create_ROA_graph():

    ROA = dcc.Graph(
        id='ROA-graph',
        style={'width': '100%'}
    )

    return ROA