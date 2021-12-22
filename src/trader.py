
import math


class Trader(object):

    def __init__(self, stop_loss, take_profit):
        super(Trader, self).__init__()
        
        self.take_profit: float = take_profit
        self.stop_loss: float = stop_loss
        self.initial_capital = 50000
        self.total_capital = self.initial_capital
        self.max_ann: float = 0.0
        self.min_ann: float = 0.0
        self.position: float = 0.0
        self.position_contracts = 0
        self.is_entry = True
        self.last_trade = 0
        self.can_trade_again = True

    def stop_loss_hit(self, close: float) -> bool:
        if not self.max_ann: return False
        alvo = self.max_ann - self.min_ann
        stop_loss_pontos = alvo * (-self.stop_loss) 
        if self.position > 0:
            stop_loss_posicao = self.position + stop_loss_pontos
            return close < stop_loss_posicao
        else:
            stop_loss_posicao = self.position + stop_loss_pontos
            return close > abs(stop_loss_posicao)

    def take_profit_hit(self, close: float) -> bool:
        alvo = self.max_ann - self.min_ann
        take_profit_pontos = alvo * (self.take_profit)
        
        if self.position > 0:
            take_profit_posicao = self.position + take_profit_pontos
            return close > take_profit_posicao
        else:
            take_profit_posicao = self.position + take_profit_pontos
            return close < abs(take_profit_posicao)


    def buy_signal(self, close: float) -> bool:
        return bool(close <= self.min_ann)


    def sell_signal(self, close: float) -> bool:
        return bool(close >= self.max_ann)


    def close_position(self, close, is_last_candle_day):
        return bool((self.take_profit_hit(close)
            or is_last_candle_day 
            or (self.stop_loss_hit(close))))

    def set_can_trade_again(self, close):
        if self.last_trade < 0:
            self.can_trade_again = close < self.max_ann
        elif self.last_trade > 0:
            self.can_trade_again = close > self.min_ann
        

    def send_order(self, close, is_last_candle_day, daily_volume):
        
        if not self.can_trade_again:
            self.set_can_trade_again(close)

        order = 0
        order_nature = ""

        if self.take_profit_hit(close) and not self.is_entry:
            order = - close * math.copysign(1, self.position)
            order_nature = "take_profit"
            self.can_trade_again = True
            self.last_trade = 0

        if self.stop_loss_hit(close) and not self.is_entry:
            order = - close * math.copysign(1, self.position)
            order_nature = "stop_loss"
            self.can_trade_again = False

        if not is_last_candle_day and self.can_trade_again and self.is_entry:
            if self.buy_signal(close):
                order_nature = "buy_signal"
                order = close
                self.position_contracts = self.total_capital // close
                if (self.position_contracts * close) > (daily_volume * .01):
                    self.position_contracts = (daily_volume * .01) // close
                self.last_trade = 1
            elif self.sell_signal(close):
                order_nature = "sell_signal"
                order = - close
                self.position_contracts = self.total_capital // close
                if (self.position_contracts * close) > (daily_volume * .01):
                    self.position_contracts = (daily_volume * .01) // close
                self.last_trade = -1

        if is_last_candle_day:
            self.can_trade_again = True
            self.last_trade = 0
            if not self.is_entry:
                order_nature = "last_candle"
                order = - close * math.copysign(1, self.position)


        if order: 
            if not self.is_entry:
                result = self.position + order
                self.total_capital -= self.position_contracts * result
            self.position = order if self.is_entry else 0
            self.is_entry = not self.is_entry


        return order, order_nature
