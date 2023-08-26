from dash import dcc, html

from utils import get_symbols, get_industries

def create_industry_dropdown():

    symbols = get_industries()
    options = [{'label':symbol, 'value':symbol} for symbol in symbols]


    return dcc.Dropdown(options, id='industry-dropdown', maxHeight=150, style={'width':'90%', 'maxWidth':'90%', 'display':'inline-block'})

def create_stock_dropdown():

    symbols = get_symbols()
    options = [{'label':symbol, 'value':symbol} for symbol in symbols]


    return dcc.Dropdown(options, id='mover-dropdown', maxHeight=300, multi=True, style={'width':'90%', 'maxWidth':'90%', 'display':'inline-block'})