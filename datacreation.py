import pandas as pd
import numpy as np
from matplotlib import pyplot
import os
from binance.client import Client


class Datacreation():
    def __init__(self, apikey, secretkey, pair, since):
        self.pair = pair
        self.since = since
        self.client = Client(apikey, secretkey)
        self.dataframe = self.client.get_historical_klines(
            self.pair, Client.KLINE_INTERVAL_1MINUTE, self.since)

    def creation(self):
        self.dataframe = pd.DataFrame(
            self.dataframe,
            columns=[
                "Open time",
                "Open",
                "High",
                "Low",
                "Close",
                "Volume",
                "Close time",
                "Quote asset volume",
                "Number of trades",
                "Taker buy base asset volume",
                "Taker buy quote asset volume",
                "Ignore",
            ],
        )
        self.dataframe.set_index("Open time", inplace=True)
        self.dataframe.to_csv(self.pair + ".csv")

    def normalize(self, dataframe):
        #scale between 0 and 1
        #Error when min and max values are the same
        result = dataframe.copy()
        for feature_name in dataframe:
            max_value = dataframe[feature_name].max()
            min_value = dataframe[feature_name].min()
            result[feature_name] = (dataframe[feature_name] -
                                    min_value) / (max_value - min_value)

        self.normalized = result
        return self.normalized

    def standardize(self):
        df = pd.read_csv(self.pair + '.csv')
        # Delete useless columns
        df.drop(['Open time', 'Close time', "Ignore"], axis=1, inplace=True)
        # Remove the trend
        result = df.copy()
        result[['Open', 'High', 'Low',
                'Close']] = result[['Open', 'High', 'Low',
                                    'Close']].diff(axis=0, periods=-1)
        result = result[:-1]
        return result

    def uniformalize(self):
        self.creation()
        result = self.normalize(self.standardize())
        result.to_csv("datafile/" + self.pair + ".csv")
        os.remove(self.pair + '.csv')
        result.plot()
        pyplot.show()
