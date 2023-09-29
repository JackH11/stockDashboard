import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

from .dropdowns import create_stock_dropdown, create_industry_dropdown


BACKGROUND_COLOR = '#1E1E24'
BORDER_COLOR = '#383838'


api_layout = html.Div(children=[
    html.Div(children=[
        html.Div(html.Div(children=[
            html.H1('Industry Data',style={'color':'white','text-align':'center'}),
            html.Div(children=[
                create_industry_dropdown(),
                html.Button("Fetch Data", id="fetch-industry-data",
                            style={'width':'25%','height':'30px','border-radius':'4px'}),
            ],style={'display':'flex','justify-content':'space-between', 'padding':'0px 50px 0px 50px'})
        ]),style={'height':'120px','width':'100%','background':BACKGROUND_COLOR, 'padding':'10px 0 30px 0',
                  'border':f'1px solid {BORDER_COLOR}','border-radius':'5px'}),
        html.Div(html.Div(children=[
            html.H1('Stock Data', style={'color': 'white', 'text-align': 'center'}),
            html.Div(children=[
                create_stock_dropdown(),
                html.Button("Fetch Data", id="api-fetch-stock-data",
                            style={'width': '25%', 'height': '30px', 'border-radius': '4px'}),
            ], style={'display': 'flex', 'justify-content': 'space-between', 'padding': '0px 50px 0px 50px'})
        ]), style={'height': '120px', 'width': '100%', 'background': BACKGROUND_COLOR, 'padding': '10px 0 30px 0',
                   'border': f'1px solid {BORDER_COLOR}', 'border-radius': '5px'}),
        html.Div(html.Div(children=[
            html.H1('All Data', style={'color': 'white', 'text-align': 'center'}),
            html.Div(children=[
                html.Button("Fetch Data", id="api-fetch-all-data",
                            style={'width': '25%', 'height': '30px', 'border-radius': '4px','margin':'auto'}),
            ], style={'display': 'flex', 'justify-content': 'space-between', 'padding': '0px 50px 0px 50px'})
        ]), style={'height': '120px', 'width': '100%', 'background': BACKGROUND_COLOR, 'padding': '10px 0 30px 0',
                   'border': f'1px solid {BORDER_COLOR}', 'border-radius': '5px'}),
        html.Div(html.Div(children=[
            html.H1('New Data', style={'color': 'white', 'text-align': 'center'}),
            html.Div(children=[
                dcc.Input(id='api-new-text',value='',type='text'),
                html.Button("Fetch Data", id="api-fetch-new-data",
                            style={'width': '25%', 'height': '30px', 'border-radius': '4px'}),
            ], style={'display': 'flex', 'justify-content': 'space-between', 'padding': '0px 50px 0px 50px'})
        ]), style={'height': '120px', 'width': '100%', 'background': BACKGROUND_COLOR, 'padding': '10px 0 30px 0',
                   'border': f'1px solid {BORDER_COLOR}', 'border-radius': '5px'}),
    ]
    ,style={'width':'50%','background':BACKGROUND_COLOR,'display': 'flex', 'flex-direction': 'column', 'align-items': 'center', 'justify-content': 'space-between', 'padding':'50px 40px 50px 40px'}),
    html.Div('',id='fetch-output',style={'height':'100vh','width':'50%','background':'green'}),
    html.Div(id='dummy-output1'),
    html.Div(id='dummy-output2'),
    html.Div(id='dummy-output3')


],style={'display':'flex','height':'100vh'})