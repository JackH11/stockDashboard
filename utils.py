import psycopg2
import pandas as pd
from psycopg2 import errorcodes

def get_connection():

    conn = psycopg2.connect(
        host='localhost',
        port='5432',
        database='exchangedata',
        user='postgres',
        password='begin1'

    )

    return conn

def log_table_updates(conn, table:str, ticker:str):

    cursor = conn.cursor()

    sql = f"INSERT INTO last_updated (\"table\",symbol,last_updated) \
                VALUES ('{table}','{ticker}',NOW()) \
                ON CONFLICT (\"table\",symbol) \
                DO UPDATE SET last_updated = NOW()"

    try:
        cursor.execute(sql)
    except psycopg2.IntegrityError as e:
        print(f"Error has occured while logging the date for table: {table} and ticker {ticker}", e)

    conn.commit()

def float_to_int_string(float_str):
    try:
        float_val = float(float_str)
        int_val = int(float_val)
        int_str = str(int_val)
        return int_str
    except ValueError:
        # Handle the case where the input is not a valid float string
        return '0'


def get_stock_data(conn, table, tickers=[]):
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

def fetch_columns(conn,table,columns=None,where=''):

    cursor = conn.cursor()
    if columns:
        columns = ','.join(column for column in columns)
    else:
        columns = '*'

    query = f"SELECT {columns} FROM {table} {where}"
    cursor.execute(query)

    rows = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]

    cursor.close()
    conn.close()

    df = pd.DataFrame(rows, columns=column_names)

    return df



def get_symbols():

    conn = get_connection()
    cursor = conn.cursor()

    query = 'SELECT DISTINCT symbol FROM symbols;'
    cursor.execute(query)

    rows = cursor.fetchall()
    rows = list(map(lambda x: x[0], rows))

    cursor.close()

    return rows

def get_industries():

    conn = get_connection()
    cursor = conn.cursor()

    query = 'SELECT DISTINCT industry FROM industries;'
    cursor.execute(query)

    rows = cursor.fetchall()
    rows = list(map(lambda x: x[0], rows))

    cursor.close()
    return rows

def add_symbol(conn, ticker):

    cursor = conn.cursor()

    sql = f"INSERT INTO symbols (symbol) VALUES ('{ticker}')"

    try:
        cursor.execute(sql)
    except psycopg2.IntegrityError as e:
        if e.pgcode == errorcodes.UNIQUE_VIOLATION:
            # Handling the UniqueViolation error
            pass
        else:
            # Handling other types of IntegrityError
            return f"An integrity error occurred while adding a new symbol {e}"


    cursor.close()

    return f"Successfully added new symbol {ticker}"



def get_updated_date(conn, ticker:str, table:str) -> str:


    cursor = conn.cursor()

    sql = f"SELECT last_updated FROM last_updated WHERE symbol = {ticker} AND table = {table}"

    try:
        cursor.execute(sql)
    except psycopg2.IntegrityError as e:
        return f"An integrity error occurred while adding a new symbol {e}"

    cursor.close()

    rows = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]

    df = pd.DataFrame(rows, columns=column_names)


    if df.empty:
        return "No Update Date was found"
    else:
        return df.loc[0, 'last_updated']






