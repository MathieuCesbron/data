import pandas as pd
from binance.client import Client
import keys


class Datacreation():
    def __init__(self, apikey, secretkey, pair, since):
        self.pair = pair
        self.since = since
        self.client = Client(apikey, secretkey)


newdata = Datacreation(keys.apiKey, keys.secretKey, "BNBUSDT",
                       "1 hour ago UTC")

print(newdata.client)
