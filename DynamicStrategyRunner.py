import json
import backtrader as bt
from datetime import datetime
from datetime import date
import pandas as pd

from DynamicStrategy import DynamicStrategy
# from shared.enums import TimeFrame

class DynamicStrategyRunner():

    # def run(self, symbol, strategy_config, interval=TimeFrame.DAILY, start_date=date(2000,1,1), end_date = date.today()):
    def run(self, symbol, strategy_config):
        cerebro = bt.Cerebro()

        # cerebro.adddata(self.getDataFromFile(symbol, interval, start_date, end_date))
        cerebro.adddata(self.getDataFromFile(symbol))

        # Add dynamically created strategy
        cerebro.addstrategy(DynamicStrategy, config=strategy_config)

        self.set_broker_param(cerebro, strategy_config)

        print(f"Starting Portfolio Value: {cerebro.broker.getvalue()}")

        cerebro.run()
        # self.order_details(cerebro)
        print(f"Final Portfolio Value: {cerebro.broker.getvalue()}")
        return {'closingcash': cerebro.broker.getvalue()}

    def set_broker_param(self, cerebro ,strategy_config):
        if "broker_params" in strategy_config:
            broker_params = strategy_config["broker_params"]
            if "cash" in broker_params:
                cerebro.broker.set_cash(broker_params["cash"])
            if "commission" in broker_params:
                cerebro.broker.setcommission(commission=broker_params["commission"])


    def getDataFromFile(self, symbol):
        # df = pd.read_csv('D:/Development/Code/Trading/zone-marker/backend/data/priceData/NSE/HDFCBANK/1d.csv')
        df = pd.read_csv('C:/workspace/python/algotrading/HDFCBANK_daily_data.csv')

        df.rename(columns={'Date': 'date', 'Open': 'open'
            , 'Close': 'close', 'High': 'high',
                           'Low': 'low', 'Volume': 'volume'}, inplace=True)

        df['datetime'] = pd.to_datetime(df['date'])
        # df['datetime'] = df['datetime'].dt
        df['openinterest'] = 0

        df = df[['datetime', 'open', 'high', 'low', 'close', 'volume', 'openinterest']]
        df.set_index('datetime', inplace=True)

        # Create a Data Feed
        data = bt.feeds.PandasDirectData(
            dataname=df)
        return data

    def order_details(self, cerebro):
        data = []
        for order in cerebro.strategy.orders:
            print(order)
        return data

if __name__ == "__main__":
    with open("strategy.json", "r") as f:
        strategy_config = json.load(f)
    DynamicStrategyRunner().run('HDFCBANK', strategy_config)