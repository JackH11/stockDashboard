import dash
from dash import dcc, html, Input, Output, State
import pandas as pd
import plotly.express as px

from plotly.subplots import make_subplots
import plotly.graph_objects as go

from utils import fetch_columns, get_connection

from Individual_Stock.layout import individual_layout
from Individual_Stock.graphs.earningsPerShare import fetch_data
from Individual_Stock.graphs.ROA import fetch_ROA_data
from Individual_Stock.graphs.PE import fetch_PE_data
from Individual_Stock.graphs.debtToEquity import fetch_debtToEquity_data
from Individual_Stock.graphs.weeklyStockPrice import fetch_weekly_data, adjust_stock_split

from Industry_Data.graphs.earningsPerShare import fetch_earnings_data
from Industry_Data.graphs.ROA import fetch_ROAs_data
from Industry_Data.graphs.debtToEquity import fetch_debtToEquitys_data
from Industry_Data.layout import industry_layout

from Market_Movements.layout import movements_layout



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
    Input('layout-toggle', 'data')
)
def update_earnings_graph(n_intervals,active_layout):

    if active_layout == 2:
        return dash.no_update

    df = fetch_data()

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
                    'text':'ROA',
                    'font': {'color': 'white'}
                },
                'tickfont': {'color': 'white'},
                'showgrid': False,
                'zeroline': False,

            },
            'yaxis': {
                'title': {
                    'text':'ROA',
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
    Input('layout-toggle', 'data')
)
def update_ROA_graph(n_intevals,active_layout):

    if active_layout == 2:
        return dash.no_update

    df = fetch_ROA_data()

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
                    'text':'ROA',
                    'font': {'color': 'white'}
                },
                'tickfont': {'color': 'white'},
                'showgrid':False,
                'zeroline': False,

            },
            'yaxis': {
                'title': {
                    'text':'ROA',
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
    Input('layout-toggle', 'data')
)
def update_PE_graph(n_intervals, active_layout):

    if active_layout == 2:
        return dash.no_update

    df = fetch_PE_data()

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
                    'text':'ROA',
                    'font': {'color': 'white'}
                },
                'tickfont': {'color': 'white'},
                'showgrid': False,
                'zeroline': False,

            },
            'yaxis': {
                'title': {
                    'text':'ROA',
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
    Input('layout-toggle', 'data')
)
def update_debtToEquity_graph(n_intervals, active_layout):

    if active_layout == 2:
        return dash.no_update

    df = fetch_debtToEquity_data()

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
                    'text':'ROA',
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
    Input('interval','n_intervals'),
    Input('layout-toggle', 'data')
)
def update_weekly_graph(n_intervals, active_layout):

    if active_layout == 2:
        return dash.no_update

    df = fetch_weekly_data()

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
                    'text':'ROA',
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

# industry
@app.callback(
    Output('earnings-subplot','figure'),
    [Input('interval','n_intervals'),
     Input('stock-dropdown', 'value'),
     Input('layout-toggle', 'data')]
)
def update_earnings_industry_graph(n_intervals, tickers, active_layout):

    if active_layout == 1:
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
    [Output('debtToEquity-graph1','figure'),
     Output('debtToEquity-graph2','figure'),
     Output('debtToEquity-graph3','figure'),
     Output('debtToEquity-graph4','figure')],
    [Input('interval','n_intervals'),
     Input('stock-dropdown', 'value'),
     Input('layout-toggle', 'data')]
)
def update_debtToEquitys_graph(n_intervals, tickers, active_layout):

    if active_layout == 1:
        return dash.no_update

    if tickers is None:
        tickers = []

    figures = []
    for i in range(4):

        if i >= len(tickers):
            df = fetch_debtToEquitys_data('')
        else:
            df = fetch_debtToEquitys_data(tickers[i])

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
                    'text': '',
                    'font': {'color': 'white'}
                },
                'xaxis': {
                    'title': {
                        'text': '',
                        'font': {'color': 'white'}
                    },
                    'tickfont': {'color': 'white'},
                    'showgrid': False,
                    'zeroline': False,
                },
                'yaxis': {
                    'title': {
                        'text': 'Debt to Equity' if i == 0 else '',
                        'font': {'color': 'white'}
                    },
                    'tickfont': {'color': 'white'},
                    'showgrid': False,
                    'zeroline': False,
                },
                'plot_bgcolor': BACKGROUND_COLOR,  # Set the plot background color
                'paper_bgcolor': PAPER_COLOR,
                'margin': {'l': 50, 'r': 10, 't':60, 'b':40}
            }
        }

        figures.append(figure)

    return figures

# industry
@app.callback(
    [Output('ROA-graph1', 'figure'),
     Output('ROA-graph2', 'figure'),
     Output('ROA-graph3', 'figure'),
     Output('ROA-graph4', 'figure')],
    [Input('interval', 'n_intervals'),
     Input('stock-dropdown', 'value'),
     Input('layout-toggle', 'data')]
)
def update_stock_dropdown(n_intevals, tickers, active_layout):

    if active_layout == 1:
        return dash.no_update

    if tickers is None:
        tickers = []

    figures = []
    for i in range(4):

        if i >= len(tickers):
            df = fetch_ROAs_data('')
        else:
            df = fetch_ROAs_data(tickers[i])

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
                        'text': '',
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
                        'text': 'ROA' if i == 0 else '',
                        'font': {'color': 'white'}
                    },
                    'tickfont': {'color': 'white'},
                    'showgrid':False,
                    'zeroline': False,

                },
                'plot_bgcolor': BACKGROUND_COLOR,  # Set the plot background color
                'paper_bgcolor': PAPER_COLOR,
                'margin': {'l': 50, 'r': 10, 't':60, 'b':40}
            }
        }

        figures.append(figure)

    return figures

# industry
@app.callback(
    [Output('stock-dropdown', 'value')],
    [Input('industry-dropdown', 'value'),
     Input('layout-toggle', 'data')]
)
def update_industry_dropdown(industry,active_layout):

    if active_layout == 1:
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
    Input('layout-toggle', 'data')
)
def toggle_layout(toggle_individual, toggle_industry, toggle_movers, active_layout):

    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]


    if changed_id == 'toggle-button.n_clicks':
        return individual_layout, 1
    elif changed_id == 'toggle-button2.n_clicks' and active_layout != 2:
        return industry_layout, 2
    elif changed_id == 'toggle-button3.n_clicks' and active_layout != 3:
        return movements_layout, 3


    return dash.no_update, dash.no_update


@app.callback(
    Output('mover-graph', 'figure'),
    [Input('interval', 'n_intervals'),
     Input('mover-dropdown', 'value'),
     Input('layout-toggle', 'data')]
)
def update_mover_dropdown(n_intevals, tickers, active_layout):


    if active_layout == 2:
        return dash.no_update

    df = fetch_weekly_data()

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
                'text': 'Debt to Equity',
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




# Create the layout for the dashboard
app.layout = html.Div(children=[
    html.Link(href='https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.1/normalize.min.css', rel='stylesheet'),
    dcc.Store(id='layout-toggle', data=1),
    dcc.Interval(id='interval',interval=5000, n_intervals=0),
    html.Div(children=[
        html.Button("Individual Stock", id="toggle-button",style={'width':'33.33%','height':'30px','border-radius':'0px','border-width':'0 1px 0 0'}),
        html.Button("Industry", id="toggle-button2",style={'width':'33.33%','height':'30px','border-radius':'0px','border-width':'0 1px 0 1px'}),
        html.Button("Large Movements", id="toggle-button3",style={'width':'33.33%','height':'30px','border-radius':'0px','border-width':'0 0 0 1px'}),
    ],style={'display':'flex'}),
    html.Div(id='dynamic-layout')
    ],
    style={
        'margin': '0',  # Reset margin for the entire layout
        'height': '100vh',  # Make sure the layout fills the viewport height
    })

if __name__ == '__main__':
    app.run_server(debug=True)
