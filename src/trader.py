from fastquant import CustomStrategy, BaseStrategy
from fastquant.indicators import MACD, CrossOver 
from fastquant.indicators.custom import CustomIndicator


# Create a subclass of the BaseStrategy, We call this MAMAStrategy (MACD + ALMA)
class MAMAStrategy(BaseStrategy):
    
    params = (
        ("alma_column", "alma"),   # name for the ALMA column from the dataframe
        ("macd_fast_period", 12),  # period for the MACD
        ("macd_slow_period", 16),
        ("macd_signal_period",9)
    )

    def __init__(self):
        # Initialize global variables
        super().__init__()
        
        # Setup MACD indicator parameters
        self.macd_fast_period = self.params.macd_fast_period
        self.macd_slow_period = self.params.macd_slow_period
        self.macd_signal_period = self.params.macd_signal_period
       
        
        # Setup MACD indicator, macd line and macd signal line, and macd signal line crossover
        self.macd_ind = MACD(
            period_me1=self.macd_fast_period, 
            period_me2=self.macd_slow_period, 
            period_signal=self.macd_signal_period
        )
        self.macd = self.macd_ind.macd
        self.macd_signal = self.macd_ind.signal
        
        # Add signal line cross over
        self.macd_signal_crossover = CrossOver(
            self.macd_ind, self.macd_signal
        )
        
        # Assign ALMA column from the dataframe
        self.alma_column = self.params.alma_column
        
        # Set ALMA indicator from the alma column of data
        self.alma = CustomIndicator(
            self.data, custom_column=self.alma_column,
        )
        
        # Plot the ALMA indicator along with the price instead of a separate plot
        self.alma.plotinfo.subplot = False
        self.alma.plotinfo.plotname = "ALMA"

        print("===Strategy level arguments===")
        print("PARAMS: ", self.params)
        

    # Buy when the custom indicator is below the lower limit, and sell when it's above the upper limit
    def buy_signal(self) -> bool:
        alma_buy =  self.dataclose[0] > self.alma[0]    # Close is above ALMA
        macd_buy = self.macd_signal_crossover > 0       # MACD crosses signal line upward
        
        
        return alma_buy and macd_buy 
    def sell_signal(self)-> bool:
        return self.alma[0] > self.dataclose[0]


class Trader(object):
    \item Comprar quando fechamento $\leq$ $min_{ANN}$, vender quando fechamento $\geq$ $max_{ANN}$;
    \item Comprar quando fechamento $\leq$ $min_{ANN}$, vender no último minuto do dia;
    \item Comprar quando fechamento $\leq$ $min_{ANN}$, vender com preço de stop-loss;
    """docstring for Trader."""
    def __init__(self, arg, stop_loss, initial_capital):
        super(Trader, self).__init__()
        self.arg = arg
        self.stop_loss = stop_loss
        self.initial_capital = initial_capital
        self.total_capital = initial_capital
    
    '''
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

        
