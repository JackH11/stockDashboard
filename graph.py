import asyncio

import dash
from dash import dcc, html, Input, Output, State
import pandas as pd
import plotly.express as px
import time

from plotly.subplots import make_subplots
import plotly.graph_objects as go

from utils import fetch_columns, get_connection, add_symbol

from Individual_Stock.layout import individual_layout
from Individual_Stock.graphs.earningsPerShare import fetch_individual_earnings_data
from Individual_Stock.graphs.ROA import fetch_ROA_data
from Individual_Stock.graphs.PE import fetch_PE_data
from Individual_Stock.graphs.debtToEquity import fetch_debtToEquity_data
from Individual_Stock.graphs.weeklyStockPrice import fetch_weekly_data, adjust_stock_split

from Industry_Data.graphs.earningsPerShare import fetch_earnings_data
from Industry_Data.graphs.ROA import fetch_ROAs_data
from Industry_Data.graphs.debtToEquity import fetch_debtToEquitys_data
from Industry_Data.layout import industry_layout

from Market_Movements.layout import movements_layout

from API.layout import api_layout
from API.fetch_data.fetch_cashflow import fetch_cashflow
from API.fetch_data.fetch_earnings import fetch_earnings
from API.fetch_data.fetch_weekly_stock import fetch_weekly_stock
from API.fetch_data.fetch_balance_sheet import fetch_balance_sheet
from API.fetch_data.fetch_income_statement import fetch_income_statement
from API.fetch_data.fetch_daily_stock import fetch_daily_stock
from API.fetch_data.fetch_all_data import fetch_all_data_api, fetch_to_update_data, update_specific_table


PAPER_COLOR = '#1E1E24'
BACKGROUND_COLOR = '#1E1E24'


COLOR_ONE = '#ff85fe'
COLOR_TWO = '#bb48fe'
COLOR_THREE = '#6a00ff'
COLOR_FOUR = '#0d7cff'


# Create the Plotly Dash app
app = dash.Dash(__name__)


# individual stock
@app.callback(
    Output('earnings-graph', 'figure'),
    Input('interval', 'n_intervals'),
    Input('dropdown','value'),
    Input('layout-toggle', 'data')
)
def update_earnings_graph(n_intervals,ticker,active_layout):

    if active_layout != 1:
        return dash.no_update

    df = fetch_individual_earnings_data(ticker)

    figure = {
        'data': [{'x': df['fiscal_date_ending'],
                 'y': df['reported_eps'],
                'mode': 'markers', 'name': f'Estimated EPS - GOOGL',
                'marker': {
                    'color': COLOR_ONE,  # Set marker color to blue
                    'size': 7,       # Set marker size
                    'opacity': 0.7,
                }
            }],
        'layout': {
            'title': {
                    'text':'Earnings Per Share',
                    'font': {'color': 'white'}
                },
            'xaxis': {
                'title': {
                    'text':'Fiscal End Date',
                    'font': {'color': 'white'}
                },
                'tickfont': {'color': 'white'},
                'showgrid': False,
                'zeroline': False,

            },
            'yaxis': {
                'title': {
                    'text':'',
                    'font': {'color': 'white'}
                },
                'tickfont': {'color': 'white'},
                'showgrid': False,
                'zeroline': False,

            },
            'plot_bgcolor': BACKGROUND_COLOR,
            'paper_bgcolor': PAPER_COLOR
        }

    }

    return figure

# individual stock
@app.callback(
    Output('ROA-graph','figure'),
    Input('interval','n_intervals'),
    Input('dropdown','value'),
    Input('layout-toggle', 'data')
)
def update_ROA_graph(n_intervals,ticker,active_layout):

    if active_layout != 1:
        return dash.no_update

    df = fetch_ROA_data(ticker)

    figure = {
        'data': [{'x': df['fiscal_date_ending'],
                 'y': df['ROA'],
                 'mode': 'markers', 'name': f'Estimated EPS - GOOGL',
                 'marker': {
                      'color': COLOR_TWO,  # Set marker color to blue
                      'size': 7,  # Set marker size
                      'opacity': 0.7,
                  }
                  }],
        'layout': {
            'title': {
                    'text':'ROA',
                    'font': {'color': 'white'}
                },
            'xaxis': {
                'title': {
                    'text':'Fiscal End Date',
                    'font': {'color': 'white'}
                },
                'tickfont': {'color': 'white'},
                'showgrid':False,
                'zeroline': False,

            },
            'yaxis': {
                'title': {
                    'text':'',
                    'font': {'color': 'white'}
                },
                'tickfont': {'color': 'white'},
                'showgrid':False,
                'zeroline': False,

            },
            'plot_bgcolor': BACKGROUND_COLOR,  # Set the plot background color
            'paper_bgcolor': PAPER_COLOR
        }
    }

    return figure

# individual stock
@app.callback(
    Output('PE-graph','figure'),
    Input('interval','n_intervals'),
    Input('dropdown','value'),
    Input('layout-toggle', 'data')
)
def update_PE_graph(n_intervals,ticker, active_layout):

    if active_layout != 1:
        return dash.no_update

    df = fetch_PE_data(ticker)

    figure = {
        'data': [{'x': df['fiscal_date_ending'],
                  'y': df['PE'],
                  'mode': 'markers', 'name': f'Estimated EPS - GOOGL',
                  'marker': {
                      'color': COLOR_THREE,  # Set marker color to blue
                      'size': 7,  # Set marker size
                      'opacity': 0.7,
                  }
                  }],
        'layout': {
            'title': {
                    'text':'PE',
                    'font': {'color': 'white'}
                },
            'xaxis': {
                'title': {
                    'text':'Fiscal End Date',
                    'font': {'color': 'white'}
                },
                'tickfont': {'color': 'white'},
                'showgrid': False,
                'zeroline': False,

            },
            'yaxis': {
                'title': {
                    'text':'',
                    'font': {'color': 'white'}
                },
                'tickfont': {'color': 'white'},
                'showgrid': False,
                'zeroline': False,

            },
            'plot_bgcolor': BACKGROUND_COLOR,  # Set the plot background color
            'paper_bgcolor': PAPER_COLOR
        }
    }

    return figure

# indivudual stock
@app.callback(
    Output('debtToEquity-graph','figure'),
    Input('interval','n_intervals'),
    Input('dropdown','value'),
    Input('layout-toggle', 'data')
)
def update_debtToEquity_graph(n_intervals,ticker, active_layout):

    if active_layout != 1:
        return dash.no_update

    df = fetch_debtToEquity_data(ticker)

    figure = {
        'data': [{'x': df['fiscal_date_ending'],
                  'y': df['debtToEquity'],
                  'mode': 'markers', 'name': f'Estimated EPS - GOOGL',
                  'marker': {
                      'color': COLOR_FOUR,  # Set marker color to blue
                      'size': 7,  # Set marker size
                      'opacity': 0.7,
                  }
                  }],
        'layout': {
            'title': {
                    'text':'Debt to Equity',
                    'font': {'color': 'white'}
                },
            'xaxis': {
                'title': {
                    'text':'Fiscal End Date',
                    'font': {'color': 'white'}
                },
                'tickfont': {'color': 'white'},
                'showgrid':False,
                'zeroline': False,
            },
            'yaxis': {
                'title': {
                    'text':'',
                    'font': {'color': 'white'}
                },
                'tickfont': {'color': 'white'},
                'showgrid':False,
                'zeroline': False,
            },
            'plot_bgcolor': BACKGROUND_COLOR,  # Set the plot background color
            'paper_bgcolor': PAPER_COLOR
        }
    }

    return figure

# individual stock
@app.callback(
    Output('weekly-stock-graph','figure'),
    Output('ticker-header','children'),
    Output('stock-price','children'),
    Input('interval','n_intervals'),
    Input('dropdown','value'),
    Input('layout-toggle', 'data')
)
def update_weekly_graph(n_intervals, ticker, active_layout):

    if active_layout != 1:
        return dash.no_update, dash.no_update, dash.no_update

    df = fetch_weekly_data(ticker)

    #df = adjust_stock_split(df)

    figure = {
        'data': [{'x': df['etimestamp'],
                  'y': df['eclose'],
                  'mode': 'lines', 'name': f'Estimated EPS - GOOGL',
                  'marker': {
                      'color': COLOR_FOUR,  # Set marker color to blue
                      'size': 7,  # Set marker size
                      'opacity': 0.7,
                  }
                  }],
        'layout': {
            'title': {
                    'text':'Debt to Equity',
                    'font': {'color': 'white'}
                },
            'xaxis': {
                'title': {
                    'text':'Fiscal End Date',
                    'font': {'color': 'white'}
                },
                'tickfont': {'color': 'white'},
                'showgrid':False,
                'zeroline': False,
            },
            'yaxis': {
                'title': {
                    'text':'',
                    'font': {'color': 'white'}
                },
                'tickfont': {'color': 'white'},
                'showgrid':False,
                'zeroline': False,
            },
            'plot_bgcolor': BACKGROUND_COLOR,  # Set the plot background color
            'paper_bgcolor': PAPER_COLOR
        }
    }

    # Getting the most recent stock price
    if (len(df) > 0):
        latest_stock_index = df['etimestamp'].idxmax()
        price = df.loc[latest_stock_index, 'eclose']
    else:
        price = ''

    value = f"${price} Up 10.3%"

    return figure, ticker, value

# industry
@app.callback(
    Output('earnings-subplot','figure'),
    [Input('interval','n_intervals'),
     Input('stock-dropdown', 'value'),
     Input('layout-toggle', 'data')]
)
def update_earnings_industry_graph(n_intervals, tickers, active_layout):

    if active_layout != 2:
        return dash.no_update

    if tickers is None:
        tickers = []

    fig = make_subplots(rows=1,cols=4,subplot_titles=tickers, shared_yaxes=True)

    for i in range(4):

        if i >= len(tickers):
            df = fetch_earnings_data('')
            title = ''
        else:
            df = fetch_earnings_data(tickers[i])
            title = tickers[i]


        scatter = go.Scatter(
            x=df['fiscal_date_ending'],
            y=df['reported_eps'],
            mode='markers',
            name=f'Estimated EPS - {title}',
            marker={
                'color': COLOR_ONE,
                'size': 7,
                'opacity': 0.7,
            }
        )

        fig.add_trace(scatter, row=1, col=i + 1)

        if i < len(tickers):
            fig.layout.annotations[i].update(font=dict(color='white'))

        fig.update_xaxes(title={'text':'','font': {'color': 'white'}}, showgrid=False, zeroline=False, tickfont=dict(color='white'), row=1, col=i + 1)
        fig.update_yaxes(title={'text':'EPS' if i == 0 else '','font': {'color': 'white'}}, showgrid=False, zeroline=False, tickfont=dict(color='white'), row=1, col=i + 1)



    fig.update_layout(
        title=dict(text='Earnings Subplots', x=0.5 , font=dict(color='white')),
        showlegend=False,
        plot_bgcolor=BACKGROUND_COLOR,
        paper_bgcolor=PAPER_COLOR,
        margin={'l': 50, 'r': 10, 't': 60, 'b': 40},
    )

    return fig

# industry
@app.callback(
     Output('debtToEquity-subplot','figure'),
    [Input('interval','n_intervals'),
     Input('stock-dropdown', 'value'),
     Input('layout-toggle', 'data')]
)
def update_debtToEquitys_graph(n_intervals, tickers, active_layout):

    if active_layout != 2:
        return dash.no_update

    if tickers is None:
        tickers = []

    fig = make_subplots(rows=1,cols=4,subplot_titles=tickers, shared_yaxes=True)

    for i in range(4):

        if i >= len(tickers):
            df = fetch_debtToEquitys_data('')
            title = ''
        else:
            df = fetch_debtToEquitys_data(tickers[i])
            title = tickers[i]


        scatter = go.Scatter(
            x=df['fiscal_date_ending'],
            y=df['debtToEquity'],
            mode='markers',
            name=f'Estimated EPS - {title}',
            marker={
                'color': COLOR_TWO,
                'size': 7,
                'opacity': 0.7,
            }
        )

        fig.add_trace(scatter, row=1, col=i + 1)

        if i < len(tickers):
            fig.layout.annotations[i].update(font=dict(color='white'))

        fig.update_xaxes(title={'text':'','font': {'color': 'white'}}, showgrid=False, zeroline=False, tickfont=dict(color='white'), row=1, col=i + 1)
        fig.update_yaxes(title={'text':'Debt to Equity' if i == 0 else '','font': {'color': 'white'}}, showgrid=False, zeroline=False, tickfont=dict(color='white'), row=1, col=i + 1)



    fig.update_layout(
        title=dict(text='Debt to Equity', x=0.5 , font=dict(color='white')),
        showlegend=False,
        plot_bgcolor=BACKGROUND_COLOR,
        paper_bgcolor=PAPER_COLOR,
        margin={'l': 50, 'r': 10, 't': 60, 'b': 40},
    )

    return fig



# industry
@app.callback(
    Output('roa-subplot', 'figure'),
    [Input('interval', 'n_intervals'),
     Input('stock-dropdown', 'value'),
     Input('layout-toggle', 'data')]
)
def update_stock_dropdown(n_intervals, tickers, active_layout):


    if active_layout != 2:
        return dash.no_update

    if tickers is None:
        tickers = []

    fig = make_subplots(rows=1,cols=4,subplot_titles=tickers, shared_yaxes=True)

    for i in range(4):

        if i >= len(tickers):
            df = fetch_ROAs_data('')
            title = ''
        else:
            df = fetch_ROAs_data(tickers[i])
            title = tickers[i]


        scatter = go.Scatter(
            x=df['fiscal_date_ending'],
            y=df['ROA'],
            mode='markers',
            name=f'Estimated EPS - {title}',
            marker={
                'color': COLOR_THREE,
                'size': 7,
                'opacity': 0.7,
            }
        )

        fig.add_trace(scatter, row=1, col=i + 1)

        if i < len(tickers):
            fig.layout.annotations[i].update(font=dict(color='white'))

        fig.update_xaxes(title={'text':'Fiscal End Date','font': {'color': 'white'}}, showgrid=False, zeroline=False, tickfont=dict(color='white'), row=1, col=i + 1)
        fig.update_yaxes(title={'text':'ROA' if i == 0 else '','font': {'color': 'white'}}, showgrid=False, zeroline=False, tickfont=dict(color='white'), row=1, col=i + 1)



    fig.update_layout(
        title=dict(text='Return on Assets', x=0.5 , font=dict(color='white')),
        showlegend=False,
        plot_bgcolor=BACKGROUND_COLOR,
        paper_bgcolor=PAPER_COLOR,
        margin={'l': 50, 'r': 10, 't': 60, 'b': 40},
    )

    return fig


# industry
@app.callback(
    [Output('stock-dropdown', 'value')],
    [Input('industry-dropdown', 'value'),
     Input('layout-toggle', 'data')]
)
def update_industry_dropdown(industry,active_layout):

    if active_layout != 2:
        return dash.no_update


    conn = get_connection()
    df = fetch_columns(conn,'industries',['symbol'],f"WHERE industry = '{industry}'")
    tickers = list(df['symbol'])

    return [tickers]

# industry_layout
@app.callback(
    Output('dynamic-layout', 'children'),
    Output('layout-toggle','data'),
    Input('toggle-button', 'n_clicks'),
    Input('toggle-button2', 'n_clicks'),
    Input('toggle-button3', 'n_clicks'),
    Input('toggle-button4', 'n_clicks'),
    Input('layout-toggle', 'data')
)
def toggle_layout(toggle_individual, toggle_industry, toggle_movers, toggle_api, active_layout):

    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]


    if changed_id == 'toggle-button.n_clicks':
        return individual_layout, 1
    elif changed_id == 'toggle-button2.n_clicks' and active_layout != 2:
        return industry_layout, 2
    elif changed_id == 'toggle-button3.n_clicks' and active_layout != 3:
        return movements_layout, 3
    elif changed_id == 'toggle-button4.n_clicks' and active_layout != 4:
        return api_layout, 4


    return dash.no_update, dash.no_update


@app.callback(
    Output('mover-graph', 'figure'),
    [Input('interval', 'n_intervals'),
     Input('mover-dropdown', 'value'),
     Input('layout-toggle', 'data')]
)
def update_mover_dropdown(n_intervals, ticker, active_layout):

    if active_layout != 3:
        return dash.no_update

    df = fetch_weekly_data(ticker)

    # df = adjust_stock_split(df)

    figure = {
        'data': [{'x': df['etimestamp'],
                  'y': df['eclose'],
                  'mode': 'lines', 'name': f'Estimated EPS - GOOGL',
                  'marker': {
                      'color': COLOR_FOUR,  # Set marker color to blue
                      'size': 7,  # Set marker size
                      'opacity': 0.7,
                  }
                  }],
        'layout': {
            'title': {
                'text': 'Weekly Stock Price',
                'font': {'color': 'white'}
            },
            'xaxis': {
                'title': {
                    'text': 'Fiscal End Date',
                    'font': {'color': 'white'}
                },
                'tickfont': {'color': 'white'},
                'showgrid': False,
                'zeroline': False,
            },
            'yaxis': {
                'title': {
                    'text': 'ROA',
                    'font': {'color': 'white'}
                },
                'tickfont': {'color': 'white'},
                'showgrid': False,
                'zeroline': False,
            },
            'plot_bgcolor': BACKGROUND_COLOR,  # Set the plot background color
            'paper_bgcolor': PAPER_COLOR
        }
    }

    return figure


log_messages = []
async def asynchronous_task(tickers,new=False):


    # Iterate through tickers
        # call the "fetch cashflow function"
        # Log the result in the log messages
        # Sleep for 14 seconds

        # call the

    conn = get_connection()

    for ticker in tickers:

        if new:
            result = add_symbol(conn, ticker)
            log_messages.append(result)


        # cashflow
        result = fetch_cashflow(conn, ticker)
        log_messages.append(result)
        await asyncio.sleep(14)

        # income_statement
        result = fetch_income_statement(conn, ticker)
        log_messages.append(result)
        await asyncio.sleep(14)

        # balance_sheet
        result = fetch_balance_sheet(conn, ticker)
        log_messages.append(result)
        await asyncio.sleep(14)

        # earnings
        result = fetch_earnings(conn, ticker)
        log_messages.append(result)
        await asyncio.sleep(14)

        # weekly stock data
        result = fetch_weekly_stock(conn, ticker)
        log_messages.append(result)
        await asyncio.sleep(14)


        # daily stock data
        result = fetch_daily_stock(conn, ticker)
        log_messages.append(result)
        await asyncio.sleep(14)


    conn.close()


async def fetch_all_data_async(conn):


    df = fetch_to_update_data(conn)

    for index, row in df.iterrows():

        result = update_specific_table(conn,row)
        log_messages.append(result)
        await asyncio.sleep(14)

    conn.close()


@app.callback(
    Output('dummy-output1','children'),
    [Input('fetch-industry-data','n_clicks'),
     Input('api-industry-dropdown','value'),
     Input('api-stock-dropdown','value'),
     Input('api-fetch-stock-data','n_clicks')]
)
def fetch_data(toggle_industry,industry,stock,toggle_stock):

    conn = get_connection()
    df = fetch_columns(conn, 'industries', ['symbol'], f"WHERE industry = '{industry}'")
    tickers = list(df['symbol'])

    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]

    if changed_id == 'fetch-industry-data.n_clicks':
        asyncio.run(asynchronous_task(tickers))
    elif changed_id == 'api-fetch-stock-data.n_clicks':
        asyncio.run(asynchronous_task([stock]))

@app.callback(
    Output('fetch-output','children'),
    [Input('log-update-interval','n_intervals')]
)
def display_log_messages(n_intervals):

    if not log_messages:
        return "No logs found"

    logs = []

    for message in log_messages:
        logs.append(html.Div(message))
        logs.append(html.Br())

    return logs

@app.callback(
    Output('dummy-output2','children'),
    State('api-new-text','value'),
    Input('api-fetch-new-data','n_clicks')
)
def call_new_value(value,n_clicks):


    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]


    if changed_id == 'api-fetch-new-data.n_clicks':

        asyncio.run(asynchronous_task([value],new=True))

@app.callback(
    Output('dummy-output3','children'),
    Input('api-fetch-all-data','n_clicks')
)
def fetch_all_data(n_clicks):

    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]




    if changed_id == 'api-fetch-all-data.n_clicks':

        conn = get_connection()
        #asyncio.run(fetch_all_data_api(conn))
        asyncio.run(fetch_all_data_async(conn))








# Create the layout for the dashboard
app.layout = html.Div(children=[
    html.Link(href='https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.1/normalize.min.css', rel='stylesheet'),
    dcc.Store(id='layout-toggle', data=1),
    dcc.Interval(id='interval',interval=5000, n_intervals=0),
    dcc.Interval(id='log-update-interval',interval=2000),
    html.Div(children=[
        html.Button("Individual Stock", id="toggle-button",style={'width':'25%','height':'30px','border-radius':'0px','border-width':'0 1px 0 0'}),
        html.Button("Industry", id="toggle-button2",style={'width':'25%','height':'30px','border-radius':'0px','border-width':'0 1px 0 1px'}),
        html.Button("Large Movements", id="toggle-button3",style={'width':'25%','height':'30px','border-radius':'0px','border-width':'0 1px 0 1px'}),
        html.Button("API Calls", id="toggle-button4",style={'width':'25%','height':'30px','border-radius':'0px','border-width':'0 0 0 1px'}),
    ],style={'display':'flex'}),
    html.Div(id='dynamic-layout')
    ],
    style={
        'margin': '0',  # Reset margin for the entire layout
        'height': '100vh',  # Make sure the layout fills the viewport height
    })

if __name__ == '__main__':
    app.run_server(debug=True)
