import backtrader as bt
import datetime
import yfinance as yf

class VolumeStrategy(bt.Strategy):
    params = (
        ("volume_lookback", 20),
        ("buy_threshold", 1.5),  # Adjust this threshold as needed
    )

    def __init__(self):
        self.volume_avg = bt.indicators.SimpleMovingAverage(
            self.data.volume, period=self.params.volume_lookback
        )

    def next(self):
        # if self.data.volume > self.params.buy_threshold * self.volume_avg:  # Code with threshold added
        if self.data.volume > self.volume_avg:
            self.buy()

# Create a Backtrader Cerebro engine
cerebro = bt.Cerebro()

# Add a data feed (use your own data here)
# data = bt.feeds.YahooFinanceData(dataname="AAPL", fromdate=datetime.datetime(2022, 1, 1), todate=datetime.datetime(2023, 1, 1))
data = bt.feeds.PandasData(dataname=yf.download("AAPL", 
                                            start="2018-01-01", 
                                            end="2018-12-31",auto_adjust=True))
cerebro.adddata(data)

# Add the strategy to Cerebro
cerebro.addstrategy(VolumeStrategy)

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
