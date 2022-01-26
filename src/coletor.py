from datetime import datetime
import pandas as pd
import MetaTrader5 as mt5
from ta.volatility import BollingerBands, SMAIndicator

def collect_data():
    if not mt5.initialize():
        print("initialize() failed")
        mt5.shutdown()

    account = 76056949
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
        [
            mt5.TIMEFRAME_M5,
            "M5"
        ],
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
        "ITUB4",
        "BBDC4",
        "VALE3",
        "PETR4",
        "ABEV3",
        "BBAS3"
    ]
    end_date = datetime(2022, 1, 19)

    for stock in stocks:
        for timeframe in timeframes:
            rates = []
            rates = mt5.copy_rates_from(stock, timeframe[0], end_date, 99999)
            if len(rates):
                print(f"Tamanho dos dados de {stock}_{timeframe[1]}: {len(rates)}")

                rates_frame = pd.DataFrame(rates)
                if stock == "WIN@N":
                    rates_frame[["open","high","low","close"]] = rates_frame[["open","high","low","close"]] * 0.2
                if stock == "WDO@N":
                    rates_frame[["open","high","low","close"]] = rates_frame[["open","high","low","close"]] * 10
                
                # Initialize Bollinger Bands Indicator
                indicator_bb = BollingerBands(close=rates_frame["close"], window=5, window_dev=2)

                # Add Bollinger Bands features
                rates_frame['bb_bbh'] = indicator_bb.bollinger_hband()
                rates_frame['bb_bbl'] = indicator_bb.bollinger_lband()
                rates_frame = rates_frame.dropna()



                if timeframe[1] == "D1":
                    rates_frame = rates_frame[rates_frame["time"] > 1482278400]
                    rates_frame.to_csv(f"../data/{stock.replace('@N', '')}_{timeframe[1]}_without.csv",
                                    index=False, header=None)
                else:
                    rates_frame = rates_frame[rates_frame["time"] > 1547859661]
                rates_frame.to_csv(f"../data/{stock.replace('@N', '')}_{timeframe[1]}.csv",
                                index=False)

    mt5.shutdown()
