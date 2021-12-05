

class Trader(object):
    """
    \item Comprar quando fechamento $\leq$ $min_{ANN}$, vender quando fechamento $\geq$ $max_{ANN}$
    \item Comprar quando fechamento $\leq$ $min_{ANN}$, vender no último minuto do dia
    \item Comprar quando fechamento $\leq$ $min_{ANN}$, vender com preço de stop-loss
    """

    def __init__(self, min_ann, max_ann, stop_loss):
        super(Trader, self).__init__()
        self.stop_loss: float = stop_loss
        # self.initial_capital = initial_capital
        # self.total_capital = initial_capital
        self.max_ann: float = max_ann
        self.min_ann: float = min_ann
        self.position: float = 0.0

    def did_stop_loss_hit(self, close: float) -> bool:
        alvo = self.max_ann - self.min_ann

        if self.position > 0:
            stop_loss_pontos = alvo * (self.stop_loss - 100)
            stop_loss_posicao = self.position + stop_loss_pontos
            return close < stop_loss_posicao
        else:
            stop_loss_pontos = alvo * (self.stop_loss - 100)
            stop_loss_posicao = self.position - stop_loss_pontos
            return close > stop_loss_posicao


        return False

    def buy_signal(self, close: float, min_ann: float, is_last_candle_day: bool) -> bool:
        if ((close <= min_ann) or (is_last_candle_day and self.position) or (self.did_stop_loss_hit(close))):
            return True
        return False

    '''
    \item Vender quando fechamento $\geq$ $max_{ANN}$, comprar quando fechamento $\leq$ $min_{ANN}$;
    \item Vender quando fechamento $\geq$ $max_{ANN}$, comprar no último minuto do dia;
    \item Vender quando fechamento $\geq$ $max_{ANN}$, comprar com preço de stop-loss. 
    '''

    def sell_signal(self, close: float, max_ann: float, is_last_candle_day: bool) -> bool:
        if close >= max_ann or (is_last_candle_day and self.position) or self.did_stop_loss_hit(close):
            return True
        return False
