import requests, psycopg2, json
from psycopg2 import errorcodes

from utils import float_to_int_string, log_table_updates


def fetch_income_statement(conn, ticker):

    print('- ' *15 + "STARTING INCOME STATEMENT" + '- ' *15)

    int_columns = [
        "gross_profit",
        "total_revenue",
        "cost_of_revenue",
        "cost_of_goods_and_services_sold",
        "operating_income",
        "selling_general_and_administrative",
        "research_and_development",
        "operating_expenses",
        "investment_income_net",
        "net_interest_income",
        "interest_income",
        "interest_expense",
        "non_interest_income",
        "other_non_operating_income",
        "depreciation",
        "depreciation_and_amortization",
        "income_before_tax",
        "income_tax_expense",
        "interest_and_debt_expense",
        "net_income_from_continuing_operations",
        "comprehensive_income_net_of_tax",
        "ebit",
        "ebitda",
        "net_income"]

    print(ticker)

    cursor = conn.cursor()

    url = "https://www.alphavantage.co/query"

    params = {
        "function": "INCOME_STATEMENT",
        "symbol": ticker,
        "apikey": "SYFIFCQ6K4QYHX7J",
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
        "reported_currency",
        "gross_profit",
        "total_revenue",
        "cost_of_revenue",
        "cost_of_goods_and_services_sold",
        "operating_income",
        "selling_general_and_administrative",
        "research_and_development",
        "operating_expenses",
        "investment_income_net",
        "net_interest_income",
        "interest_income",
        "interest_expense",
        "non_interest_income",
        "other_non_operating_income",
        "depreciation",
        "depreciation_and_amortization",
        "income_before_tax",
        "income_tax_expense",
        "interest_and_debt_expense",
        "net_income_from_continuing_operations",
        "comprehensive_income_net_of_tax",
        "ebit",
        "ebitda",
        "net_income"
    ]

    reports = data['quarterlyReports']

    for report in reports:

        sql = f"INSERT INTO income_statement_quarterly ({', '.join(columns)}) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        data_values = [ticker,
                       report["fiscalDateEnding"], report["reportedCurrency"], report["grossProfit"],
                       report["totalRevenue"], report["costOfRevenue"],
                       report["costofGoodsAndServicesSold"], report["operatingIncome"],
                       report["sellingGeneralAndAdministrative"], report["researchAndDevelopment"],
                       report["operatingExpenses"], report["investmentIncomeNet"], report["netInterestIncome"],
                       report["interestIncome"], report["interestExpense"],
                       report["nonInterestIncome"], report["otherNonOperatingIncome"],
                       report["depreciation"], report["depreciationAndAmortization"],
                       report["incomeBeforeTax"] ,report["incomeTaxExpense"], report["interestAndDebtExpense"],
                       report["netIncomeFromContinuingOperations"] ,report["comprehensiveIncomeNetOfTax"],
                       report["ebit"] ,report["ebitda"], report["netIncome"]
                       ]

        for index ,value in enumerate(data_values):
            if value == 'None':
                data_values[index] = '0'
            if columns[index] in int_columns:
                data_values[index] = float_to_int_string(data_values[index])

        try:
            cursor.execute(sql, data_values)
        except psycopg2.IntegrityError as e:
            if e.pgcode == errorcodes.UNIQUE_VIOLATION:
                # Handling the UniqueViolation error
                pass
            else:
                # Handling other types of IntegrityError
                return f"An integrity error occurred during income statement {e}"


        conn.commit()

    cursor.close()

    log_table_updates(conn,'income_statement_quarterly',ticker)

    return f"Uploaded income statement data for ticker {ticker}"
