import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

from .dropdowns import create_stock_dropdown
from .graphs.weeklyStockPrice import create_weekly_graph



BACKGROUND_COLOR = '#1E1E24'




movements_layout = html.Div(children=[

    html.Div(children=[
            html.Div(children=[html.Div('Stocks',style={'margin-bottom':'20px'}),
                               create_stock_dropdown()
            ],style={'background':'blue','width':'300px','height':'30%', 'align-items': 'center', 'display': 'flex', 'justify-content': 'center','flex-direction': 'column'}),
        ],style={'width':'30%','background':BACKGROUND_COLOR, 'display': 'flex', 'flex-direction': 'column', 'align-items': 'center', 'justify-content': 'space-between', 'padding':'80px 0px 300px 0px'}),
        create_weekly_graph()
], style={'display':'flex','height':'100vh'})