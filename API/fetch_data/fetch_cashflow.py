import requests, psycopg2, json
from psycopg2 import errorcodes

from utils import float_to_int_string, log_table_updates


def fetch_cashflow(conn,ticker):

    #print('- ' *15 + "STARTING CASHFLOW" + '- ' *15)

    int_columns = ['reported_currency' ,'operating_cashflow' ,'payments_for_operating_activities',
                   'proceeds_from_operating_activities' ,'change_in_operating_liabilities'
                   ,'change_in_operating_assets',
                   'depreciation_depletion_and_amortization' ,'capital_expenditures' ,'change_in_receivables'
                   ,'change_in_inventory',
                   'profit_loss' ,'cashflow_from_investment' ,'cashflow_from_financing'
                   ,'proceeds_from_repayments_of_short_term_debt',
                   'payments_for_repurchase_of_common_stock' ,'payments_for_repurchase_of_equity'
                   ,'payments_for_repurchase_of_preferred_stock',
                   'dividend_payout' ,'dividend_payout_common_stock' ,'dividend_payout_preferred_stock'
                   ,'proceeds_from_issuance_of_common_stock',
                   'proceeds_from_issuance_of_long_term_debt_and_capital_securities'
                   ,'proceeds_from_issuance_of_preferred_stock',
                   'proceeds_from_repurchase_of_equity' ,'proceeds_from_sale_of_treasury_stock'
                   ,'change_in_cash_and_cash_equivalents',
                   'change_in_exchange_rate' ,'net_income']

    #print(ticker)

    cursor = conn.cursor()

    url = "https://www.alphavantage.co/query"

    params = {
        "function": "CASH_FLOW",
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

    columns = ['fiscal_date_ending' ,'reported_currency' ,'operating_cashflow' ,'payments_for_operating_activities',
               'proceeds_from_operating_activities' ,'change_in_operating_liabilities'
               ,'change_in_operating_assets',
               'depreciation_depletion_and_amortization' ,'capital_expenditures' ,'change_in_receivables'
               ,'change_in_inventory',
               'profit_loss' ,'cashflow_from_investment' ,'cashflow_from_financing'
               ,'proceeds_from_repayments_of_short_term_debt',
               'payments_for_repurchase_of_common_stock' ,'payments_for_repurchase_of_equity'
               ,'payments_for_repurchase_of_preferred_stock',
               'dividend_payout' ,'dividend_payout_common_stock' ,'dividend_payout_preferred_stock'
               ,'proceeds_from_issuance_of_common_stock',
               'proceeds_from_issuance_of_long_term_debt_and_capital_securities'
               ,'proceeds_from_issuance_of_preferred_stock',
               'proceeds_from_repurchase_of_equity' ,'proceeds_from_sale_of_treasury_stock'
               ,'change_in_cash_and_cash_equivalents',
               'change_in_exchange_rate' ,'net_income' ,'symbol']

    reports = data['quarterlyReports']

    for report in reports:

        sql = f"INSERT INTO cashflow_quarterly ({', '.join(columns)}) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        data_values = [
            report["fiscalDateEnding"], report["reportedCurrency"], report["operatingCashflow"],
            report["paymentsForOperatingActivities"], report["proceedsFromOperatingActivities"],
            report["changeInOperatingLiabilities"], report["changeInOperatingAssets"],
            report["depreciationDepletionAndAmortization"], report["capitalExpenditures"],
            report["changeInReceivables"], report["changeInInventory"], report["profitLoss"],
            report["cashflowFromInvestment"], report["cashflowFromFinancing"],
            report["proceedsFromRepaymentsOfShortTermDebt"], report["paymentsForRepurchaseOfCommonStock"],
            report["paymentsForRepurchaseOfEquity"], report["paymentsForRepurchaseOfPreferredStock"],
            report["dividendPayout"], report["dividendPayoutCommonStock"], report["dividendPayoutPreferredStock"],
            report["proceedsFromIssuanceOfCommonStock"],
            report["proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet"],
            report["proceedsFromIssuanceOfPreferredStock"], report["proceedsFromRepurchaseOfEquity"],
            report["proceedsFromSaleOfTreasuryStock"], report["changeInCashAndCashEquivalents"],
            report["changeInExchangeRate"], report["netIncome"] ,[ticker][0]
        ]

        for index, value in enumerate(data_values):
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
                return f"An integrity error occurred during cashflow {e}"
                print("An integrity error occurred:", e)


        conn.commit()

    cursor.close()

    log_table_updates(conn,'cashflow_quarterly',ticker)

    return f"Uploaded cashflow data for ticker {ticker}"
