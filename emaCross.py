import backtrader as bt
from datetime import datetime
import yfinance as yf

# class EMACrossoverStrategy(bt.Strategy):
#     params = (
#         ("short_period", 20),
#         ("long_period", 50),
#     )

#     def __init__(self):
#         short_ma = bt.indicators.ExponentialMovingAverage(
#             self.data.close, period=self.params.short_period
#         )
#         long_ma = bt.indicators.ExponentialMovingAverage(
#             self.data.close, period=self.params.long_period
#         )

#         self.crossover = bt.indicators.CrossOver(short_ma, long_ma)

#     def next(self):
#         if self.crossover > 0:
#             # EMA crossover, buy signal
#             self.buy()
#         elif self.crossover < 0:
#             # EMA crossover, sell signal
#             self.sell()

# if __name__ == "__main__":
#     # Create a Backtrader Cerebro engine
#     cerebro = bt.Cerebro()
#     # Add a data feed (use your own data here)
#     # data = bt.feeds.YahooFinanceData(dataname="AAPL", fromdate=datetime(2018, 1, 1), todate=datetime(2021, 12, 31))
#     data = bt.feeds.PandasData(dataname=yf.download("AAPL", 
#                                             start="2018-01-01", 
#                                             end="2018-12-31",auto_adjust=True))
#     cerebro.adddata(data)

#     # Add the strategy to Cerebro
#     cerebro.addstrategy(EMACrossoverStrategy)

#     # Set the initial cash amount for the backtest
#     cerebro.broker.set_cash(100000)

#     # Print the starting cash amount
#     print("Starting Portfolio Value: %.2f" % cerebro.broker.getvalue())

#     # Run the backtest
#     cerebro.run()

#     # Print the ending cash amount
#     print("Ending Portfolio Value: %.2f" % cerebro.broker.getvalue())

#     # Plot the backtest results
#     cerebro.plot(style="candlestick")

class EMAStrategy(bt.Strategy):
    params = (
        ("short_period", 6),
        ("medium_period", 14),
        ("long_period", 27),
    )

    def __init__(self):
        self.ema_short = bt.indicators.ExponentialMovingAverage(self.data.close, period=self.params.short_period)
        self.ema_medium = bt.indicators.ExponentialMovingAverage(self.data.close, period=self.params.medium_period)
        self.ema_long = bt.indicators.ExponentialMovingAverage(self.data.close, period=self.params.long_period)
        
        print("self.ema_short",self.params.short_period)

    def next(self):
        if self.ema_short > self.ema_medium > self.ema_long and self.position:
            self.sell()

        elif self.ema_short < self.ema_medium < self.ema_long and not self.position:
            self.buy()

if __name__ == "__main__":
    cerebro = bt.Cerebro()

    # Add a data feed
    # data = bt.feeds.YahooFinanceData(dataname="AAPL", fromdate=datetime(2021, 1, 1), todate=datetime(2022, 1, 1))
    data = bt.feeds.PandasData(dataname=yf.download("AAPL", 
                                            start="2018-01-01", 
                                            end="2018-12-31",auto_adjust=True))
    cerebro.adddata(data)

    # Add the strategy with custom parameters
    cerebro.addstrategy(EMAStrategy, short_period=5, medium_period=13, long_period=26)

    # Set the initial cash amount for the backtest
    cerebro.broker.set_cash(100000)

    # Set commission
    cerebro.broker.setcommission(commission=0.001)

    # Print the starting cash amount
    print(f"Starting Portfolio Value: {cerebro.broker.getvalue()}")

    # Run the backtest
    cerebro.run()

    # Print the final cash amount
    print(f"Ending Portfolio Value: {cerebro.broker.getvalue()}")
