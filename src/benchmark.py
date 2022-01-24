import pandas as pd
from ta.trend import SMAIndicator


class Benchmark(object):
    """docstring for Forecasting."""

    def __init__(self):
        super(Benchmark, self).__init__()

    def sma_5(self, rates_frame, window=5):
        sma_5_low = SMAIndicator(
            close=rates_frame["low"], window=window).sma_indicator()
        sma_5_high = SMAIndicator(
            close=rates_frame["high"], window=window).sma_indicator()
        result = pd.DataFrame([rates_frame["time"], sma_5_low, sma_5_high, rates_frame["low"],
                              rates_frame["high"], rates_frame["real_volume"]]).transpose().dropna().reset_index(drop=True)
        result.columns = ['time', 'min_ann',
                          'max_ann', 'low', 'high', 'real_volume']
        return result

    def sma_10(self, rates_frame, window=10):
        sma_5_low = SMAIndicator(
            close=rates_frame["low"], window=window).sma_indicator()
        sma_5_high = SMAIndicator(
            close=rates_frame["high"], window=window).sma_indicator()
        result = pd.DataFrame([rates_frame["time"], sma_5_low, sma_5_high, rates_frame["low"],
                              rates_frame["high"], rates_frame["real_volume"]]).transpose().dropna().reset_index(drop=True)
        result.columns = ['time', 'min_ann',
                          'max_ann', 'low', 'high', 'real_volume']
        return result

    def sma_20(self, rates_frame, window=20):
        sma_5_low = SMAIndicator(
            close=rates_frame["low"], window=window).sma_indicator()
        sma_5_high = SMAIndicator(
            close=rates_frame["high"], window=window).sma_indicator()
        result = pd.DataFrame([rates_frame["time"], sma_5_low, sma_5_high, rates_frame["low"],
                              rates_frame["high"], rates_frame["real_volume"]]).transpose().dropna().reset_index(drop=True)
        result.columns = ['time', 'min_ann',
                          'max_ann', 'low', 'high', 'real_volume']
        return result

    def one_day_lag(self, rates_frame):
        sma_5_low = rates_frame["low"].shift(periods=1)
        sma_5_high = rates_frame["high"].shift(periods=1)
        result = pd.DataFrame([rates_frame["time"], sma_5_low, sma_5_high, rates_frame["low"],
                              rates_frame["high"], rates_frame["real_volume"]]).transpose().dropna().reset_index(drop=True)
        result.columns = ['time', 'min_ann',
                          'max_ann', 'low', 'high', 'real_volume']
        return result
