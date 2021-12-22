from datetime import datetime
import pandas as pd
import MetaTrader5 as mt5

def collect_data():
    if not mt5.initialize():
        print("initialize() failed")
        mt5.shutdown()

    account = 66056949
    authorized = mt5.login(account, server="XPMT5-DEMO")
    if authorized:
        print("connected to account #{}".format(account))
    else:
        print("failed to connect at account #{}, error code: {}".format(
            account, mt5.last_error()))

    timeframes = [
        # [
        #     mt5.TIMEFRAME_M1,
        #     "M1"
        # ],
        # [
        #     mt5.TIMEFRAME_M5,
        #     "M5"
        # ],
        [
            mt5.TIMEFRAME_M15, 
            "M15"
        ],
        [
            mt5.TIMEFRAME_D1,
            "D1"
        ],
    ]

    stocks = [
        "WIN@N",
        "WDO@N",
        "VALE3",
        "PETR4",
        "CASH3",
        "MGLU3",
    ]
    end_date = datetime(2021, 11, 1)

    for stock in stocks:
        for timeframe in timeframes:
            rates = []
            rates = mt5.copy_rates_from(stock, timeframe[0], end_date, 99999)
            if len(rates):
                print(f"Tamanho dos dados de {stock}_{timeframe[1]}: {len(rates)}")

                rates_frame = pd.DataFrame(rates)
                if timeframe[1] == "D1":
                    rates_frame.to_csv(f"../data/{stock.replace('@N', '')}_{timeframe[1]}_without.csv",
                                    index=False, header=None)
                rates_frame.to_csv(f"../data/{stock.replace('@N', '')}_{timeframe[1]}.csv",
                                index=False)

    mt5.shutdown()
