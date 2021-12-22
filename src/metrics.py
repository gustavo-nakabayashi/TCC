def calc_drawdawn(df_orders_summary):
    previous_peaks = (df_orders_summary["cum_result"]).cummax()
    maximum_drawdown = (df_orders_summary["cum_result"] - previous_peaks)
    maximum_drawdown_percentage = (maximum_drawdown / previous_peaks) * 100
    return maximum_drawdown, maximum_drawdown_percentage

def success_rate(df_orders_summary):
    positive_trades = len(df_orders_summary[df_orders_summary["result"] > 0])
    total_trades = len(df_orders_summary)
    return (positive_trades/total_trades) * 100

def annualized_return(initial_capital, df_orders_summary):
    
    total_days = (df_orders_summary["time"].iloc[-1].date() - df_orders_summary["time"].iloc[0].date()).days
    final_capital = df_orders_summary["cum_result"].iloc[-1]

    ra = 100 * ((final_capital/initial_capital)**(365.25/total_days) - 1)
    return ra