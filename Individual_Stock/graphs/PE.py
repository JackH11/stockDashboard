from dash import dcc, html
import pandas as pd

from utils import get_stock_data,get_connection

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

PE = dcc.Graph(
    id='pe-graph',
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
            'title': 'PE',
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
            'paper_bgcolor': '#d3d3d3'
        },

    },
    style={'width':'100%'}
)


def fetch_PE_data():
    ticker = 'GOOGL'
    conn = get_connection()
    all_eps = get_stock_data(conn, 'earnings_report_quarterly', [ticker])
    all_eps['fiscal_date_ending'] = pd.to_datetime(all_eps['fiscal_date_ending'])

    conn = get_connection()
    all_stocks = get_stock_data(conn, 'stock_history_daily', [ticker])

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