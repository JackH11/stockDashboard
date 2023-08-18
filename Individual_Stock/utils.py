import psycopg2
import pandas as pd

def get_connection():
    conn = psycopg2.connect(
        host='localhost',
        port='5432',
        database='exchangedata',
        user='postgres',
        password='begin1'

    )

    return conn


def get_data(conn, table, tickers=[]):
    cursor = conn.cursor()

    if len(tickers) == 1:
        query = f"SELECT * FROM {table} WHERE symbol = '{tickers[0]}';"
    elif len(tickers) > 1:
        ticker_str = ','.join("'" + ticker + "'" for ticker in tickers)
        query = f"SELECT * FROM {table} WHERE symbol IN ({ticker_str});"
    else:
        query = f"SELECT * FROM {table};"

    cursor.execute(query)

    rows = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]

    cursor.close()
    conn.close()

    df = pd.DataFrame(rows, columns=column_names)

    return df


