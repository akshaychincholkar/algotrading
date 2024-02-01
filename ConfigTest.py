import json
import backtrader as bt

class MyApp:
    # def __init__(self, config):
    #     self.config = config
    def __init__(self, config):
        self.config = config
        self.dataclose = self.datas[0].close

        # To keep track of pending orders and buy price/commission
        self.order = None
        self.buyprice = None
        self.buycomm = None

        # Dynamic initialization of indicators based on the config
        for indicator_name, params in config.get("indicators", {}).items():
            indicator_class = getattr(bt.indicators, indicator_name)
            setattr(self, indicator_name, indicator_class(**params))

    def run(self):
        # Your application logic using the config
        print("Config:", self.config)

def main():
    # Define your JSON configuration
    # json_config = '''
    # {
    #     "app_name": "MyApp",
    #     "debug_mode": true,
    #     "max_connections": 10
    # }
    # '''

    # Parse the JSON string into a Python dictionary
    # config_dict = json.loads(json_config)

    with open('Strategy.json','r') as file:
        config_dict = json.load(file)

    # Create an instance of MyApp with the config
    my_app_instance = MyApp(config_dict)

    # Run your application
    my_app_instance.run()

if __name__ == "__main__":
    main()
