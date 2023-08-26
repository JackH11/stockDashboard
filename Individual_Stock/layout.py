import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

from .graphs.earningsPerShare import create_earnings_graph
from .graphs.ROA import create_ROA_graph
from .graphs.PE import create_PE_graph
from .graphs.debtToEquity import create_debtToEquity_graph
from .dropdown import create_stock_dropdown
from .graphs.weeklyStockPrice import create_weekly_graph


BACKGROUND_COLOR = '#1E1E24'


individual_layout = html.Div(children=[


    html.Div(children=[
        html.Div(children=[
            html.Div(children=[
                html.Div(children=[
                    html.Div(children=[
                        html.Div(
                            html.H1("Apple", style={'text-align':'left','margin':'0px','color':'white'}),
                            style={'width':'100%'}
                        ),
                        html.Div(
                            html.H3("AAPL", style={'text-align':'left','margin':'0px','color':'white'}),
                            style={'width':'100%'}
                        ),
                    ],style={'margin-right':'auto', 'margin-left':'10px'}),
                    html.Div(
                        html.H3("$187.46 Up 10.3%"),
                        style={'margin-left':'auto','color':'white'}
                    )
                ],style={'display':'flex'}),
                # First Graph - P/E Ratio
                html.Div(
                        create_weekly_graph()
                ,style={'margin-top':'20px'}),
                html.Div(
                create_stock_dropdown()
                ,style={'width':'30%','align-items':'center','display':'inline-block','margin-top':'20px'}),
            ],style={'text-align': 'center', 'maxWidth':'100%', 'margin-top':'25px'}),
        ],style={'width':'50%','background':BACKGROUND_COLOR,'text-align': 'center', 'maxWidth':'50%', 'height':'100%'}),
        html.Div(children=[
            html.Div(children=[
                create_earnings_graph(),
                create_ROA_graph()
            ], style={'display':'flex','max-height':'50%'}),
            html.Div(children=[
                create_PE_graph(),
                create_debtToEquity_graph()
            ],style={'display':'flex','max-height':'50%'})
        ],style={'width':'50%','background':'#1E1E24','padding':'10px','max-height':'100vh'})
    ],style={'display':'flex', 'height':'100vh'})
])