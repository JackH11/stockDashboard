from dash import dcc, html

from utils import get_symbols



def create_stock_dropdown():

    symbols = get_symbols()
    options = [{'label':symbol, 'value':symbol} for symbol in symbols]


    return dcc.Dropdown(options, id='dropdown', maxHeight=75, style={'width':'90%', 'maxWidth':'90%', 'display':'inline-block'})



