import requests, psycopg2, json
from psycopg2 import errorcodes

from utils import float_to_int_string, log_table_updates


def fetch_balance_sheet(conn, ticker):


    int_columns = [
        'total_assets',
        'total_current_assets',
        'cash_and_cash_equivalents_at_carrying_value',
        'cash_and_short_term_investments',
        'inventory',
        'current_net_receivables',
        'total_non_current_assets',
        'property_plant_equipment',
        'accumulated_depreciation_amortization_ppe',
        'intangible_assets',
        'intangible_assets_excluding_goodwill',
        'goodwill',
        'long_term_investments',
        'short_term_investments',
        'other_current_assets',
        'total_liabilities',
        'total_current_liabilities',
        'current_accounts_payable',
        'deferred_revenue',
        'current_debt',
        'short_term_debt',
        'total_non_current_liabilities',
        'capital_lease_obligations',
        'long_term_debt',
        'current_long_term_debt',
        'long_term_debt_noncurrent',
        'short_long_term_debt_total',
        'other_current_liabilities',
        'other_non_current_liabilities',
        'total_shareholder_equity',
        'treasury_stock',
        'retained_earnings',
        'common_stock',
        'common_stock_shares_outstanding'
    ]

    print('- ' *15 + "STARTING BALANCE SHEET" + '- ' *15)


    print(ticker)

    cursor = conn.cursor()

    url = "https://www.alphavantage.co/query"

    params = {
        "function": "BALANCE_SHEET",
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
        "reported_currency",
        "total_assets",
        "total_current_assets",
        "cash_and_cash_equivalents_at_carrying_value",
        "cash_and_short_term_investments",
        "inventory",
        "current_net_receivables",
        "total_non_current_assets",
        "property_plant_equipment",
        "accumulated_depreciation_amortization_ppe",
        "intangible_assets",
        "intangible_assets_excluding_goodwill",
        "goodwill",
        "investments",
        "long_term_investments",
        "short_term_investments",
        "other_current_assets",
        "other_non_current_assets",
        "total_liabilities",
        "total_current_liabilities",
        "current_accounts_payable",
        "deferred_revenue",
        "current_debt",
        "short_term_debt",
        "total_non_current_liabilities",
        "capital_lease_obligations",
        "long_term_debt",
        "current_long_term_debt",
        "long_term_debt_noncurrent",
        "short_long_term_debt_total",
        "other_current_liabilities",
        "other_non_current_liabilities",
        "total_shareholder_equity",
        "treasury_stock",
        "retained_earnings",
        "common_stock",
        "common_stock_shares_outstanding"
    ]

    reports = data['quarterlyReports']

    for report in reports:
        subs = '(' + '%s,  ' *(len(columns ) -1) + '%s' + ')'
        sql = f"INSERT INTO balance_sheet_quarterly ({', '.join(columns)}) VALUES {subs}"

        data_values = [ticker,
                       report["fiscalDateEnding"],
                       report["reportedCurrency"],
                       report["totalAssets"],
                       report["totalCurrentAssets"],
                       report["cashAndCashEquivalentsAtCarryingValue"],
                       report["cashAndShortTermInvestments"],
                       report["inventory"],
                       report["currentNetReceivables"],
                       report["totalNonCurrentAssets"],
                       report["propertyPlantEquipment"],
                       report["accumulatedDepreciationAmortizationPPE"],
                       report["intangibleAssets"],
                       report["intangibleAssetsExcludingGoodwill"],
                       report["goodwill"],
                       report["investments"],
                       report["longTermInvestments"],
                       report["shortTermInvestments"],
                       report["otherCurrentAssets"],
                       report["otherNonCurrentAssets"],
                       report["totalLiabilities"],
                       report["totalCurrentLiabilities"],
                       report["currentAccountsPayable"],
                       report["deferredRevenue"],
                       report["currentDebt"],
                       report["shortTermDebt"],
                       report["totalNonCurrentLiabilities"],
                       report["capitalLeaseObligations"],
                       report["longTermDebt"],
                       report["currentLongTermDebt"],
                       report["longTermDebtNoncurrent"],
                       report["shortLongTermDebtTotal"],
                       report["otherCurrentLiabilities"],
                       report["otherNonCurrentLiabilities"],
                       report["totalShareholderEquity"],
                       report["treasuryStock"],
                       report["retainedEarnings"],
                       report["commonStock"],
                       report["commonStockSharesOutstanding"]
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
                return f"An integrity error occurred during balance sheet {e}"


        conn.commit()


    cursor.close()

    log_table_updates(conn,'balance_sheet_quarterly',ticker)

    return f"Uploaded balance sheet data for ticker {ticker}"
