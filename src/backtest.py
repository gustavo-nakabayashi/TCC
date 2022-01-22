import pandas as pd


def backtest(df_close, df_forecast, trader):
    orders = []
    for index, row in df_close.iterrows():
        today = df_forecast[df_forecast["date"] == row["time"].date()]
        if not len(today["min_ann"]):
            continue
        try:
            is_last_candle_day = (
                df_close.iloc[index]["time"].date()
                != df_close.iloc[index + 1]["time"].date()
            )
        except:
            is_last_candle_day = True

        trader.min_ann = today["min_ann"].item()
        trader.max_ann = today["max_ann"].item()


        order, order_nature = trader.send_order(
            row["close"], is_last_candle_day, today["real_volume"].item()
        )

        orders.append(
            {
                "order": order,
                "order_nature": order_nature,
                "min_ann": today["min_ann"].item(),
                "max_ann": today["max_ann"].item(),
                "time": row["time"],
                "close": row["close"],
                "cum_result": trader.total_capital,
                "contracts": trader.position_contracts,
            }
        )

    df_orders_original = pd.DataFrame(orders)
    df_orders = df_orders_original[
        df_orders_original["order"] != 0
    ].reset_index(drop=True)
    df_orders_exit_order = df_orders[(df_orders.index % 2) == 0].reset_index(
        drop=True
    )
    df_orders_exit_order[
        ["exit_order", "exit_price", "exit_order_nature","cum_result", "contracts"]
    ] = (
        df_orders[(df_orders.index % 2) == 1]
        .reset_index(drop=True)
        .reset_index(drop=True)[
            ["time", "order", "order_nature", "cum_result", "contracts"]
        ]
    )
    df_orders_exit_order["result"] = -(
        df_orders_exit_order ["contracts"] * (df_orders_exit_order["order"] + df_orders_exit_order["exit_price"])
    )

    return df_orders_original, df_orders_exit_order
