import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px


BACKGROUND_COLOR = '#1E1E24'


api_layout = html.Div(children=[
    html.Div(children=[
        html.Div(html.Div(children=[
            html.H1('Industry Data',style={'background':'orange','text-align':'center'}),
            html.Div(children=[
                html.H3('Industry Dropdown'),
                html.H3('Industry Button')
            ],style={'display':'flex','justify-content':'space-between'})
        ]),style={'height':'120px','width':'100%','background':'blue', 'padding':'0 80px 20px 80px'}),
        html.Div(style={'height':'120px','width':'100%','background':'blue'}),
        html.Div(style={'height':'120px','width':'100%','background':'blue'})
    ]
    ,style={'width':'50%','background':'red','display': 'flex', 'flex-direction': 'column', 'align-items': 'center', 'justify-content': 'space-between', 'padding':'150px 40px 150px 40px'}),
    html.Div('here2',style={'height':'100vh','width':'50%','background':'green'})


],style={'display':'flex','height':'100vh'})