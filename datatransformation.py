import pandas as pd
import numpy as np
from matplotlib import pyplot

df = pd.read_csv('datafile/ETHUSDT.csv')
# Delete useless columns
df.drop(['Open time', 'Close time', "Ignore"], axis=1, inplace=True)


def normalize(df):
    #scale between 0 and 1
    #Error when min and max values are the same
    result = df.copy()
    for feature_name in df:
        max_value = df[feature_name].max()
        min_value = df[feature_name].min()
        result[feature_name] = (df[feature_name] - min_value) / (max_value -
                                                                 min_value)
    return result


def standardize(df):
    #Remove the trend
    result = df.copy()
    result[['Open', 'High', 'Low',
            'Close']] = result[['Open', 'High', 'Low',
                                'Close']].diff(axis=0, periods=-1)
    result = result[:-1]
    return result


def uniformalize(df):
    return normalize(standardize(df))


result = uniformalize(df)
result.plot()
pyplot.show()
result.to_csv("aya.csv")
