import pytest
from trader import Trader 

min_ann = 2000.0
max_ann = 3000.0
stop_loss_percentage = 0.2

trader = Trader(min_ann, max_ann, stop_loss_percentage)



def test_buy_signal_on_buy():
    
    close = 1000.0
    is_last_candle_day= False
    
    assert trader.buy_signal (close, min_ann, is_last_candle_day) == True

def test_buy_signal_on_stop_loss():
    
    trader.position = min_ann
    close = 1500.0
    is_last_candle_day= False


    assert trader.buy_signal (close, min_ann, is_last_candle_day) == True

def test_buy_signal_on_day_close():
    
    close = 2000.0
    is_last_candle_day= True
    
    assert trader.buy_signal (close, min_ann, is_last_candle_day) == True

def test_sell_signal_on_sell():
    
    close = 3200.0
    is_last_candle_day= False
    
    assert trader.sell_signal (close, max_ann, is_last_candle_day) == True

def test_sell_signal_on_stop_loss():
    
    trader.position = - max_ann
    close = 3500.0
    is_last_candle_day= False

    
    assert trader.sell_signal (close, max_ann, is_last_candle_day) == True

def test_sell_signal_on_day_close():
    
    trader.position = - max_ann
    close = 1000.0
    is_last_candle_day= True
    
    assert trader.sell_signal (close, max_ann, is_last_candle_day) == True
