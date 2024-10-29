import requests, psycopg2, json
from psycopg2 import errorcodes

from utils import float_to_int_string, log_table_updates


def fetch_daily_stock(conn, ticker):

    print('- ' *15 + "STARTING DAILY STOCK" + '- ' *15)

    print(ticker)

    cursor = conn.cursor()

    url = "https://www.alphavantage.co/query"

    params = {
        "function": "TIME_SERIES_DAILY",
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

    reports = data['Time Series (Daily)']



    for week in reports.keys():
        subs = '(' + '%s,  ' *(len(columns ) -1) + '%s' + ')'
        sql = f"INSERT INTO stock_history_daily ({', '.join(columns)}) VALUES {subs}"

        data_values = [ticker,
                       week,
                       reports[week]["1. open"],
                       reports[week]["2. high"],
                       reports[week]["3. low"],
                       reports[week]["4. close"],
                       reports[week]["5. volume"]
                       ]

        for index, value in enumerate(data_values):
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

    log_table_updates(conn, 'stock_history_daily', ticker)

    return f"Uploaded daily stock data for ticker {ticker}"
