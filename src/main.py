from trader import Trader
import pandas as pd
from datetime import date
import matplotlib.pyplot as plt
from IPython.display import display, HTML
from backtest import backtest

def main():
    trader = Trader(1)
    
    df_forecast = pd.read_csv("C:\\Users\\gustavo.barros\\Documents\\UFMG\\TCC\\previsions\\PETR4_D1_high.csv")
    df_forecast.columns = ["time", "high"]
    df_low = pd.read_csv("C:\\Users\\gustavo.barros\\Documents\\UFMG\\TCC\\previsions\\PETR4_D1_low.csv")
    df_low.columns = ["time", "low"]
    df_forecast["low"] = df_low["low"]
    df_forecast['date'] = pd.to_datetime(df_forecast['time'],unit='s').dt.date
    df_forecast = df_forecast[df_forecast['date'] > date(2021,8,29)]

    df_close = pd.read_csv("C:\\Users\\gustavo.barros\\Documents\\UFMG\\TCC\\data\\PETR4_M15_close.csv")
    df_close.columns = ["time", "close"]
    df_close['time'] = pd.to_datetime(df_close['time'],unit='s')
    
    df_orders = backtest(df_close, df_forecast, trader)

    # df_orders['order'].plot(kind='bar')
    # df_orders['bad_rate'].plot(secondary_y=True)

if __name__ == "__main__":
    main()

