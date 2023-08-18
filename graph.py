import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

from Individual_Stock.layout import layout
from Individual_Stock.graphs.earningsPerShare import fetch_data
from Individual_Stock.graphs.ROA import fetch_ROA_data
from Individual_Stock.graphs.PE import fetch_PE_data
from Individual_Stock.graphs.debtToEquity import fetch_debtToEquity_data


# Create the Plotly Dash app
app = dash.Dash(__name__)

@app.callback(
    Output('earnings-graph', 'figure'),
    Input('interval','n_intervals')
)
def update_earnings_graph(n_intervals):

    df = fetch_data()

    figure = {
        'data': [{'x': df['fiscal_date_ending'],
                 'y': df['reported_eps'],
                'mode': 'markers', 'name': f'Estimated EPS - GOOGL'}],
        'layout': {
            'title': 'Earnings Per Share',
            'xaxis': {
                'title': 'Fiscal Date Ending',
            },
            'yaxis': {
                'title': 'EPS',
            }
        }

    }

    return figure

@app.callback(
    Output('ROA-graph','figure'),
    Input('interval','n_intervals')
)
def update_ROA_graph(n_intevals):

    df = fetch_ROA_data()

    figure = {
        'data': [{'x': df['fiscal_date_ending'],
                 'y': df['ROA'],
                'mode': 'markers', 'name': f'Estimated EPS - GOOGL'}],
        'layout': {
            'title': 'ROA',
            'xaxis': {
                'title': 'Fiscal Date Ending',
            },
            'yaxis': {
                'title': 'ROA',
            },
        }
    }

    return figure


@app.callback(
    Output('PE-graph','figure'),
    Input('interval','n_intervals')
)
def update_PE_graph(n_intervals):

    df = fetch_PE_data()
    print(df)

    figure = {
        'data': [{'x': df['fiscal_date_ending'],
                  'y': df['PE'],
                  'mode': 'markers', 'name': f'Estimated EPS - GOOGL'}],
        'layout': {
            'title': 'PE',
            'xaxis': {
                'title': 'Fiscal Date Ending',
            },
            'yaxis': {
                'title': 'ROA',
            },
        }
    }

    return figure

@app.callback(
    Output('debtToEquity-graph','figure'),
    Input('interval','n_intervals')
)
def update_PE_graph(n_intervals):

    df = fetch_debtToEquity_data()
    print(df)

    figure = {
        'data': [{'x': df['fiscal_date_ending'],
                  'y': df['debtToEquity'],
                  'mode': 'markers', 'name': f'Estimated EPS - GOOGL'}],
        'layout': {
            'title': 'Debt To Equity',
            'xaxis': {
                'title': 'Fiscal Date Ending',
            },
            'yaxis': {
                'title': 'ROA',
            },
        }
    }

    return figure



# Create the layout for the dashboard
app.layout = html.Div(children=[
    html.Link(href='https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.1/normalize.min.css', rel='stylesheet'),
    layout,
    dcc.Interval(id='interval',interval=6000, n_intervals=0)
    ],
    style={
        'margin': '0',  # Reset margin for the entire layout
        'height': '100vh',  # Make sure the layout fills the viewport height
    })

if __name__ == '__main__':
    app.run_server(debug=True)
