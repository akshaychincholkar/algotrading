import json
import backtrader as bt
from datetime import datetime
class DynamicStrategy(bt.Strategy):
    def run(self):
        # Your application logic using the config
        print("Run Config:", self.config)

    def __init__(self, config):
        self.config = config
        self.dataclose = self.datas[0].close
        print("Config:", self.config)
        # To keep track of pending orders and buy price/commission
        self.order = None
        self.buyprice = None
        self.buycomm = None

        # Dynamic initialization of indicators based on the config
        for indicator_name, params in config.get("indicators", {}).items():
            indicator_class = getattr(bt.indicators, indicator_name)
            print("INDICATOR CLASS: ", indicator_class)
            print("INDICATOR NAME: ",indicator_name)
            setattr(self, indicator_name, indicator_class(**params))

    def next(self):
        #self.log('Close, %.2f' % self.dataclose[0])
        if self.order:
            return
        # Dynamic logic based on the config
        if not self.position:
            for signal in self.config.get("signals", []):
                if signal["type"] == "buy":
                    if eval(signal["condition"]):
                        self.log('BUY CREATE, %.2f' % self.dataclose[0])
                        self.buy()

                elif signal["type"] == "sell":
                    if eval(signal["condition"]):
                        self.log('SELL CREATE, %.2f' % self.dataclose[0])
                        self.sell()

    def log(self, txt, dt=None):
        ''' Logging function fot this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

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
    DynamicStrategy().run(strategy_config)