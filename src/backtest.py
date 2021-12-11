def backtest(df_close, df_forecast, trader):
    orders = []
    for index, row in df_close.iterrows():
        today = df_forecast[df_forecast["date"] == row["time"].date()]
        if not len(today["low"]): continue
        # print(today)
        try:
            is_last_candle_day = df_close.iloc[index]["time"].date() != df_close.iloc[index + 1]["time"].date()
        except:
            is_last_candle_day = True

        trader.min_ann = today["low"].item()
        trader.max_ann = today["high"].item()

        order, order_nature = trader.send_order(row["close"], 
            is_last_candle_day
        )

        orders.append({
            "order": order, 
            "order_nature": order_nature, 
            "min_ann": today["low"].item(),
            "max_ann": today["high"].item(), 
            "time": row["time"],
            "close": row["close"]
        })

    df_orders = pd.DataFrame(orders)
    df_orders = df_orders[df_orders["order"] != 0].reset_index(drop=True)
    df_orders_exit_order = df_orders[(df_orders.index % 2) == 0].reset_index(drop=True)
    df_orders_exit_order[["exit_order", "exit_price", "exit_order_nature"]] = df_orders[(df_orders.index % 2) == 1].reset_index(drop=True).reset_index(drop=True)[["time", "order", "order_nature"]]
    df_orders_exit_order["result"] = -(df_orders_exit_order["order"] + df_orders_exit_order["exit_price"])
    return df_orders_exit_order