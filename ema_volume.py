import backtrader as bt
import datetime
import yfinance as yf

class MyStrategy(bt.Strategy):
    params = (
        ("ema_short", 6),
        ("ema_medium", 14),
        ("ema_long", 27),
        ("volume_lookback", 0),
    )

    def __init__(self,**kwargs):
        print("short: ",self.params.ema_short)
        print("medium: ",self.params.ema_medium)
        print("long: ",self.params.ema_long)
        print("volume: ",self.params.volume_lookback)
        for key, value in kwargs.items():
            print(f"{key}: {value}")
        self.ema_short = bt.indicators.ExponentialMovingAverage(
            self.data.close, period=self.params.ema_short
        )
        self.ema_medium = bt.indicators.ExponentialMovingAverage(
            self.data.close, period=self.params.ema_medium
        )
        self.ema_long = bt.indicators.ExponentialMovingAverage(
            self.data.close, period=self.params.ema_long
        )

        self.volume_avg = bt.indicators.SimpleMovingAverage(
            self.data.volume, period=self.params.volume_lookback
        )    
    
    def next(self):
        
        if (
            self.data.volume > self.volume_avg
            and self.ema_short > self.ema_medium
            and self.ema_medium > self.ema_long
        ):
            self.buy()
        elif (
            self.data.volume > self.volume_avg
            and self.ema_short < self.ema_medium
            and self.ema_medium < self.ema_long
        ):
            self.sell()


class Client():

    def __init__(self):

        # Create a Backtrader Cerebro engine
        cerebro = bt.Cerebro()

        # Add a data feed (use your own data here)
        # data = bt.feeds.YahooFinanceData(dataname="AAPL", fromdate=datetime.datetime(2022, 1, 1), todate=datetime.datetime(2023, 1, 1))
        data = bt.feeds.PandasData(dataname=yf.download("AAPL", 
                                                    start="2023-01-01", 
                                                    end="2023-12-31",auto_adjust=True))

        cerebro.adddata(data)

        # Add the strategy to Cerebro
        # cerebro.addstrategy(MyStrategy, ema_short=5, ema_medium=13, volume_lookback = 20)
        cerebro.addstrategy(MyStrategy, ema_short=5, ema_medium=13, volume_lookback = 20)

        # Set the initial cash amount for the backtest
        cerebro.broker.set_cash(100000)

        # Print the starting cash amount
        print("Starting Portfolio Value: %.2f" % cerebro.broker.getvalue())

        # Run the backtest
        cerebro.run()

        # Print the ending cash amount
        print("Ending Portfolio Value: %.2f" % cerebro.broker.getvalue())

        # Plot the backtest results
        cerebro.plot(style="candlestick")

