import requests, psycopg2, json
from psycopg2 import errorcodes

from utils import float_to_int_string, log_table_updates


def fetch_weekly_stock(conn, ticker):

    print('- ' *15 + "STARTING WEEKLY STOCK" + '- ' *15)

    print(ticker)

    cursor = conn.cursor()

    url = "https://www.alphavantage.co/query"

    params = {
        "function": "TIME_SERIES_WEEKLY",
        "symbol": ticker,
        "apikey": "",
        "outputsize": "full",

    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        json_data = json.dumps(data)
        json_data = json.loads(json_data)
    else:
        print("Error", response.status_code)

    columns = [
        "symbol",
        "etimestamp",
        "eopen",
        "ehigh",
        "elow",
        "eclose",
        "evolume"
    ]

    reports = data['Weekly Time Series']



    for week in reports.keys():
        subs = '(' + '%s,  ' *(len(columns ) -1) + '%s' + ')'
        sql = f"INSERT INTO stock_history_weekly ({', '.join(columns)}) VALUES {subs}"

        data_values = [ticker,
                       week,
                       reports[week]["1. open"],
                       reports[week]["2. high"],
                       reports[week]["3. low"],
                       reports[week]["4. close"],
                       reports[week]["5. volume"]
                       ]

        for index ,value in enumerate(data_values):
            if value == 'None':
                data_values[index] = '0'

        try:
            cursor.execute(sql, data_values)
        except psycopg2.IntegrityError as e:
            if e.pgcode == errorcodes.UNIQUE_VIOLATION:
                # Handling the UniqueViolation error
                pass
            else:
                # Handling other types of IntegrityError
                #print("An integrity error occurred:", e)
                #raise ValueError("Problem while sending data to db")
                return f"An integrity error occurred during weekly stock {e}"


        conn.commit()


    cursor.close()

    log_table_updates(conn, 'stock_history_weekly', ticker)

    return f"Uploaded weekly stock data for ticker {ticker}"
