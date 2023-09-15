import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

from .dropdowns import create_stock_dropdown
from .graphs.weeklyStockPrice import create_weekly_graph



BACKGROUND_COLOR = '#1E1E24'




movements_layout = html.Div(children=[

    html.Div(children=[
        html.Div(children=[html.H1('Stocks',style={'margin-bottom':'20px','color':'white'}),
                           create_stock_dropdown()
        ],style={'width':'300px','height':'30%', 'align-items': 'center', 'display': 'flex', 'justify-content': 'center','flex-direction': 'column'}),
    ],style={'width':'30%','background':BACKGROUND_COLOR, 'display': 'flex', 'flex-direction': 'column', 'align-items': 'center', 'justify-content': 'space-between', 'padding':'300px 0px 300px 0px'}),
    html.Div(
        create_weekly_graph(),
    style={'width':'40%','height':'100vh','background':BACKGROUND_COLOR,'align-items': 'center','min-width':'400px'}),
    html.Div(children=[
        html.Div(children=[
            html.H1("Movement", id='stock-header', style={'color': 'white','margin':'auto','text-align':'center'}),
            html.H3("Value Placeholder", id='stock-header', style={'color': 'white','margin':'auto','text-align':'center'})],
            style={'width': '100%'}
        ),
        html.Div(children=[
            html.H1("Shape", id='stock-header', style={'color': 'white','margin':'auto','text-align':'center'}),
            html.H3("Value Placeholder", id='stock-header', style={'color': 'white','margin':'auto','text-align':'center'})],
            style={'width': '100%'}
        )
    ],
    style={'background':BACKGROUND_COLOR,'width':'30%','display': 'flex', 'flex-direction': 'column', 'align-items': 'center', 'justify-content': 'space-between','padding':'200px 0 200px 0'})
], style={'display':'flex','height':'100vh'})