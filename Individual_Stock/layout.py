import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

from .graphs.earningsPerShare import create_earnings_graph
from .graphs.ROA import ROA,create_ROA_graph
from .graphs.PE import PE, create_PE_graph
from .graphs.debtToEquity import create_debtToEquity_graph
from .graphs.debtToEquity import debtToEquity

# Replace this with your data retrieval functions (get_data and get_connection)
# and update the data accordingly.
tickers = ['BA', 'GE', 'MMM', 'CAT']

# Mock data for demonstration purposes
# Replace this with your actual data
pe_data = pd.DataFrame({'symbol': ['BABA', 'GE', 'MMM', 'CAT'],
                        'pe': [18.5, 12.7, 18.3, 20.1]})

# Mock data for the second graph
# Replace this with your actual data
earnings_data = pd.DataFrame({'symbol': ['BA', 'BA', 'GE', 'GE', 'MMM', 'MMM', 'CAT', 'CAT'],
                              'fiscal_date_ending': ['2023-01-01', '2023-02-01', '2023-01-01', '2023-02-01',
                                                     '2023-01-01', '2023-02-01', '2023-01-01', '2023-02-01'],
                              'estimated_eps': [2.0, 1.8, 1.2, 1.5, 2.5, 2.3, 1.9, 2.2],
                              'reported_eps': [1.8, 1.9, 1.0, 1.3, 2.2, 2.0, 1.7, 2.1]})




layout = html.Div(children=[


    html.Div(children=[

        html.Div(children=[
            html.Div(children=[
                html.Div(children=[
                    html.Div(
                        html.H1("Apple", style={'text-align':'left','margin':'0'}),
                        style={'width':'100%','background':'red'}
                    ),
                    html.Div(
                        html.H3("AAPL", style={'text-align':'left','margin':'0'}),
                        style={'width':'100%','background':'red'}
                    ),
                ],style={'margin-right':'auto'}),
                html.Div(
                    html.H3("$187.46 Up 10.3%"),
                    style={'margin-left':'auto'}
                )
            ],style={'display':'flex'}),
            # First Graph - P/E Ratio
            html.Div(
                dcc.Graph(
                    id='pe-ratio-graph',
                    figure={
                        'data': [
                            {'x': pe_data['symbol'], 'y': pe_data['pe'], 'type': 'bar', 'name': 'P/E Ratio'}
                        ],
                        'layout': {
                            'title': 'Distributed P/E',
                            'xaxis': {
                                'title': 'Ticker',
                            },
                            'yaxis': {
                                'title': 'P/E Ratio',
                            },
                        }
                    }
                ),
                style={'background':'blue','border-radius': '10px', 'border': '#ffac00 solid', 'padding': '15px'}
            ),
            dcc.Dropdown(tickers,
                         'BA',
                         id='dropdown'),
        ],style={'width':'50%','background':'green'}),
        # Second Graph - Estimated Earnings Per Share vs Actual
        html.Div(children=[
            html.Div(children=[
                create_earnings_graph(),
                create_ROA_graph()
            ], style={'display':'flex','max-height':'50%'}),
            html.Div(children=[
                create_PE_graph(),
                create_debtToEquity_graph()
            ],style={'display':'flex','max-height':'50%'})
        ],style={'width':'50%','background':'orange','padding':'10px','max-height':'100vh'})
    ],style={'display':'flex', 'height':'100vh'})
])