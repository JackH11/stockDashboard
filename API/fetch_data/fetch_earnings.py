import requests, psycopg2, json
from psycopg2 import errorcodes

from utils import float_to_int_string, log_table_updates


def fetch_earnings(conn ,ticker):

    print('- ' *15 + "STARTING EARNINGS" + '- ' *15)

    print(ticker)

    cursor = conn.cursor()

    url = "https://www.alphavantage.co/query"

    params = {
        "function": "EARNINGS",
        "symbol": ticker,
        "apikey": "",
        "outputsize": "full"
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
        "fiscal_date_ending",
        "reported_date",
        "reported_eps",
        "estimated_eps",
        "surprise",
        "surprise_percentage"
    ]

    reports = data['quarterlyEarnings']

    for report in reports:

        sql = f"INSERT INTO earnings_report_quarterly ({', '.join(columns)}) VALUES (%s, %s, %s, %s, %s, %s, %s)"

        data_values = [ticker,
                       report["fiscalDateEnding"], report["reportedDate"], report["reportedEPS"],
                       report["estimatedEPS"], report["surprise"],
                       report["surprisePercentage"]
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
                return f"An integrity error occurred during earnings {e}"


        conn.commit()


    cursor.close()

    log_table_updates(conn, 'earnings_report_quarterly', ticker)

    return f"Uploaded earnings data for ticker {ticker}"
