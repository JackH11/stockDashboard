import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

from .graphs.earningsPerShare import create_earnings_graph
from .graphs.debtToEquity import create_debtToEquity_graph
from .graphs.ROA import create_ROAs_graph

from .dropdowns import create_stock_dropdown, create_industry_dropdown



BACKGROUND_COLOR = '#1E1E24'

#earnings1, earnings2, earnings3, earnings4 = create_earnings_graph()
earnings = create_earnings_graph()
ROA1, ROA2, ROA3, ROA4 = create_ROAs_graph()
debtToEquity1, debtToEquity2, debtToEquity3, debtToEquity4 = create_debtToEquity_graph()

"""
html.Div(earnings1, style={'background':'orange','width':'250px','height':'100%'}),
            html.Div(earnings2, style={'background':'orange','width':'250px','height':'100%'}),
            html.Div(earnings3, style={'background':'orange','width':'250px','height':'100%'}),
            html.Div(earnings4, style={'background':'orange','width':'250px','height':'100%'})
"""


industry_layout = html.Div(children=[

    html.Div(children=[
            html.Div(children=[html.Div('Industries',style={'margin-bottom':'20px'}),create_industry_dropdown()
            ],style={'background':'blue','width':'300px','height':'30%', 'align-items': 'center', 'display': 'flex', 'justify-content': 'center','flex-direction': 'column'}),
            html.Div(children=[html.Div('Stocks',style={'margin-bottom':'20px'}),create_stock_dropdown()
            ],style={'background':'blue','width':'300px','height':'30%', 'align-items': 'center', 'display': 'flex', 'justify-content': 'center','flex-direction': 'column'}),
        ],style={'width':'30%','background':BACKGROUND_COLOR, 'display': 'flex', 'flex-direction': 'column', 'align-items': 'center', 'justify-content': 'space-between', 'padding':'80px 0px 300px 0px'}),
    html.Div(children=[
        html.Div(children=[
            earnings
        ], style={'background':'green', 'padding':'10px', 'padding-left':'75px','padding-right':'75px', 'display':'flex','justify-content':'space-between', 'height':'calc(33.33% - 20px)'}),
        html.Div(children=[
            html.Div(debtToEquity1,style={'background':'orange','width':'250px','height':'100%'}),
            html.Div(debtToEquity2,style={'background':'orange','width':'250px','height':'100%'}),
            html.Div(debtToEquity3,style={'background':'orange','width':'250px','height':'100%'}),
            html.Div(debtToEquity4,style={'background':'orange','width':'250px','height':'100%'})
        ], style={'background':'green', 'padding':'10px', 'padding-left':'75px','padding-right':'75px', 'display':'flex','justify-content':'space-between', 'height':'calc(33.33% - 20px)'}),
        html.Div(children=[
            html.Div(ROA1,style={'background':'orange','width':'250px','height':'100%'}),
            html.Div(ROA2,style={'background':'orange','width':'250px','height':'100%'}),
            html.Div(ROA3,style={'background':'orange','width':'250px','height':'100%'}),
            html.Div(ROA4,style={'background':'orange','width':'250px','height':'100%'})
        ], style={'background':'green', 'padding':'10px', 'padding-left':'75px','padding-right':'75px', 'display':'flex','justify-content':'space-between', 'height':'calc(33.33% - 20px)'})

    ], style={'height':'100vh','background':'blue', 'width':'70%'})

], style={'display':'flex','height':'100vh'})