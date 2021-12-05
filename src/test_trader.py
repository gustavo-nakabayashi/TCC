import pytest
from trader import Trader 

NUMBER_1 = 3.0
NUMBER_2 = 2.0



def test_buy_signal_on_buy():
    
    stop_loss_percentage = 20
    trader = Trader(stop_loss_percentage)
    close = 1000.0
    min_ann = 2000.0
    is_last_candle_day= False
    
    assert trader.buy_signal (close, min_ann, is_last_candle_day) == True

def test_buy_signal_on_stop_loss():
    
    stop_loss_percentage = 20
    trader = Trader(stop_loss_percentage)
    close = 2000.0
    min_ann = 1000.0
    is_last_candle_day= False

    
    assert trader.buy_signal (close, min_ann, is_last_candle_day) == True

def test_buy_signal_on_day_close():
    
    stop_loss_percentage = 20
    trader = Trader(stop_loss_percentage)
    close = 2000.0
    min_ann = 1000.0
    is_last_candle_day= True
    
    assert trader.buy_signal (close, min_ann, is_last_candle_day) == True

def test_sell_signal_on_sell():
    
    stop_loss_percentage = 20
    trader = Trader(stop_loss_percentage)
    close = 2000.0
    max_ann = 1000.0
    is_last_candle_day= False
    
    assert trader.sell_signal (close, max_ann, is_last_candle_day) == True

def test_sell_signal_on_stop_loss():
    
    stop_loss_percentage = 20
    trader = Trader(stop_loss_percentage)
    close = 1000.0
    max_ann = 2000.0
    is_last_candle_day= False

    
    assert trader.sell_signal (close, max_ann, is_last_candle_day) == True

def test_sell_signal_on_day_close():
    
    stop_loss_percentage = 20
    trader = Trader(stop_loss_percentage)
    close = 1000.0
    max_ann = 2000.0
    is_last_candle_day= True
    
    assert trader.sell_signal (close, max_ann, is_last_candle_day) == True
