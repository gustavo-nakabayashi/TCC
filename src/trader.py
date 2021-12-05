

class Trader(object):
    """
    \item Comprar quando fechamento $\leq$ $min_{ANN}$, vender quando fechamento $\geq$ $max_{ANN}$
    \item Comprar quando fechamento $\leq$ $min_{ANN}$, vender no último minuto do dia
    \item Comprar quando fechamento $\leq$ $min_{ANN}$, vender com preço de stop-loss
    """

    def __init__(self, stop_loss):
        super(Trader, self).__init__()
        self.stop_loss = stop_loss
        # self.initial_capital = initial_capital
        # self.total_capital = initial_capital
        self.has_open_position = True

    def did_stop_loss_hit(self, close) -> bool:
        return False

    def buy_signal(self, close, min_ann, is_last_candle_day) -> bool:
        if ((close <= min_ann) or (is_last_candle_day and self.has_open_position) or (self.did_stop_loss_hit(close))):
            return True
        return False

    '''
    \item Vender quando fechamento $\geq$ $max_{ANN}$, comprar quando fechamento $\leq$ $min_{ANN}$;
    \item Vender quando fechamento $\geq$ $max_{ANN}$, comprar no último minuto do dia;
    \item Vender quando fechamento $\geq$ $max_{ANN}$, comprar com preço de stop-loss. 
    '''

    def sell_signal(self, close, max_ann, is_last_candle_day) -> bool:
        if close >= max_ann or (is_last_candle_day and self.has_open_position) or self.did_stop_loss_hit(close):
            return True
        return False
