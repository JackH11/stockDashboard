import requests, psycopg2, json
from psycopg2 import errorcodes

import pandas as pd

import asyncio

from utils import float_to_int_string, log_table_updates

from .fetch_earnings import fetch_earnings
from .fetch_daily_stock import fetch_daily_stock
from .fetch_weekly_stock import fetch_weekly_stock
from .fetch_income_statement import fetch_income_statement
from .fetch_cashflow import fetch_cashflow
from .fetch_balance_sheet import fetch_balance_sheet


def fetch_to_update_data(conn):

    cursor = conn.cursor()

    sql = "SELECT * FROM last_updated ORDER BY last_updated ASC;"

    try:
        cursor.execute(sql)
    except psycopg2.IntegrityError as e:
        if e.pgcode == errorcodes.UNIQUE_VIOLATION:
            # Handling the UniqueViolation error
            pass
        else:
            # Handling other types of IntegrityError
            return f"An integrity error occurred during income statement {e}"

    rows = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]

    df = pd.DataFrame(rows, columns=column_names)

    cursor.close()

    return df

def update_specific_table(conn, row):


    functions = {
        "cashflow_quarterly": fetch_cashflow,
        "income_statement_quarterly": fetch_income_statement,
        "balance_sheet_quarterly": fetch_balance_sheet,
        "earnings_report_quarterly": fetch_earnings,
        "stock_history_daily": fetch_daily_stock,
        "stock_history_weekly": fetch_weekly_stock
    }

    table = row['table']
    ticker = row['symbol']

    return functions[table](conn, ticker)



async def fetch_all_data_api(conn):


    cursor = conn.cursor()

    sql = "SELECT * FROM last_updated ORDER BY last_updated ASC;"

    try:
        cursor.execute(sql)
    except psycopg2.IntegrityError as e:
        if e.pgcode == errorcodes.UNIQUE_VIOLATION:
            # Handling the UniqueViolation error
            pass
        else:
            # Handling other types of IntegrityError
            return f"An integrity error occurred during income statement {e}"

    rows = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]

    df = pd.DataFrame(rows, columns=column_names)

    cursor.close()

    functions = {
        "cashflow_quarterly": fetch_cashflow,
        "income_statement_quarterly": fetch_income_statement,
        "balance_sheet_quarterly": fetch_balance_sheet,
        "earnings_report_quarterly": fetch_earnings,
        "stock_history_daily": fetch_daily_stock,
        "stock_history_weekly": fetch_weekly_stock
    }

    for index, row in df.iterrows():
        table = row['table']
        ticker = row['symbol']

        result = functions[table](conn,ticker)
        print(result)
        await asyncio.sleep(14)


        if index >= 10:
            break

















































