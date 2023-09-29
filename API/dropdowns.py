from utils import get_symbols, get_industries
from dash import dcc, html


def create_stock_dropdown():

    symbols = get_symbols()
    options = [{'label':symbol, 'value':symbol} for symbol in symbols]


    return dcc.Dropdown(options, id='api-stock-dropdown', maxHeight=300, style={'width':'60%', 'maxWidth':'90%', 'display':'inline-block'})

def create_industry_dropdown():

    symbols = get_industries()
    options = [{'label':symbol, 'value':symbol} for symbol in symbols]


    return dcc.Dropdown(options, id='api-industry-dropdown', maxHeight=150, style={'width':'60%', 'maxWidth':'90%', 'display':'inline-block'})