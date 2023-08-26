from dash import dcc, html
import pandas as pd

from utils import get_stock_data,get_connection


def fetch_weekly_data():
    ticker = 'TSLA'
    conn = get_connection()

    stock_data = get_stock_data(conn, 'stock_history_weekly', [ticker])

    return stock_data

def create_weekly_graph():


    weekly_stock_graph = dcc.Graph(
        id='weekly-stock-graph',
        style={'padding': '15px'}
    )

    return weekly_stock_graph

def adjust_stock_split(df):
    """Adjusts for stock splits in the dataframe"""

    print(df)

    for row in df.iterrows():
        if float(row[1][10]) != 1:
            df.loc[df[2] < row[1][2], 3] /= row[1][10]
            df.loc[df[2] < row[1][2], 4] /= row[1][10]
            df.loc[df[2] < row[1][2], 5] /= row[1][10]
            df.loc[df[2] < row[1][2], 8] /= row[1][10]
    return df