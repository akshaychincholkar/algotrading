import backtrader as bt
import yfinance as yf
import datetime
import json

class MyStrategy(bt.Strategy):
    def __init__(self, config):
        pass
        # self.config = config
        # self.dataclose = self.datas[0].close

        # # To keep track of pending orders and buy price/commission
        # self.order = None
        # self.buyprice = None
        # self.buycomm = None

        # # Dynamic initialization of indicators based on the config
        # for indicator_name, params in config.get("indicators", {}).items():
        #     indicator_class = getattr(bt.indicators, indicator_name)
        #     setattr(self, indicator_name, indicator_class(**params))

    def next(self):
        pass
        #self.log('Close, %.2f' % self.dataclose[0])
        # if self.order:
        #     return
        # # Dynamic logic based on the config
        # if not self.position:
        #     for signal in self.config.get("signals", []):
        #         if signal["type"] == "buy":
        #             if eval(signal["condition"]):
        #                 self.log('BUY CREATE, %.2f' % self.dataclose[0])
        #                 self.buy()

        #         elif signal["type"] == "sell":
        #             if eval(signal["condition"]):
        #                 self.log('SELL CREATE, %.2f' % self.dataclose[0])
        #                 self.sell()

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # Buy/Sell order submitted/accepted to/by broker - Nothing to do
            return

        # Check if an order has been completed
        # Attention: broker could reject order if not enough cash
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(
                    'BUY EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                    (order.executed.price,
                     order.executed.value,
                     order.executed.comm))

                self.buyprice = order.executed.price
                self.buycomm = order.executed.comm
            else:  # Sell
                self.log('SELL EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                         (order.executed.price,
                          order.executed.value,
                          order.executed.comm))

            self.bar_executed = len(self)

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')

        self.order = None

    def notify_trade(self, trade):
        if not trade.isclosed:
            return

        self.log('OPERATION PROFIT, GROSS %.2f, NET %.2f' %
                 (trade.pnl, trade.pnlcomm))                        

if __name__ == "__main__":
    print("Bhau barobar ahe!")
    with open('Strategy.json','r') as file:
        strategy_config = json.load(file)
    # MyStrategy(strategy_config).run()
# def download_data():
#     # Define the stock code (HDFCBANK) and time frame
#     stock_code = "HDFCBANK.NS"
#     start_date = datetime.datetime(2020, 1, 1)
#     end_date = datetime.datetime(2023, 1, 1)

#     # Download historical data from Yahoo Finance
#     data = yf.download(stock_code, start=start_date, end=end_date)

#     # Save data to a CSV file
#     data.to_csv("HDFCBANK_daily_data.csv")

# def run_backtest():
#     # Load data from the saved CSV file
#     data = bt.feeds.GenericCSVData(
#         dataname="HDFCBANK_daily_data.csv",
#         fromdate=datetime.datetime(2020, 1, 1),
#         todate=datetime.datetime(2023, 1, 1),
#         nullvalue=0.0,
#         dtformat="%Y-%m-%d",
#         datetime=0,
#         high=2,
#         low=3,
#         open=1,
#         close=4,
#         volume=5,
#         openinterest=-1,
#     )

#     # Create a Backtrader Cerebro engine
#     cerebro = bt.Cerebro()

#     # Add the data to the engine
#     cerebro.adddata(data)

#     # Add the strategy to the engine
#     cerebro.addstrategy(MyStrategy)

#     # Print the starting cash
#     print("Starting Portfolio Value: %.2f" % cerebro.broker.getvalue())

#     # Run the backtest
#     cerebro.run()

#     # Print the final cash
#     print("Ending Portfolio Value: %.2f" % cerebro.broker.getvalue())

# if __name__ == "__main__":
#     # Download data from Yahoo Finance and save it to a CSV file
#     download_data()

#     # Run Backtrader backtest using the saved CSV file
#     run_backtest()
