
class Trader(object):
    """docstring for Trader."""
    def __init__(self, arg, stop_loss, initial_capital):
        super(Trader, self).__init__()
        self.arg = arg
        self.stop_loss = stop_loss
        self.initial_capital = initial_capital
        self.total_capital = initial_capital
    
    '''
    \item Comprar quando fechamento $\leq$ $min_{ANN}$, vender quando fechamento $\geq$ $max_{ANN}$;
    \item Comprar quando fechamento $\leq$ $min_{ANN}$, vender no último minuto do dia;
    \item Comprar quando fechamento $\leq$ $min_{ANN}$, vender com preço de stop-loss;
    '''
    def should_enter_trade() -> bool:
        pass
    
    '''
    \item Vender quando fechamento $\geq$ $max_{ANN}$, comprar quando fechamento $\leq$ $min_{ANN}$;
    \item Vender quando fechamento $\geq$ $max_{ANN}$, comprar no último minuto do dia;
    \item Vender quando fechamento $\geq$ $max_{ANN}$, comprar com preço de stop-loss. 
    '''
    def should_leave_trade() -> bool:
        pass

        
