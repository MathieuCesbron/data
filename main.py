from binance.client import Client
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from matplotlib import pyplot
import pandas as pd
import keys

#Changes these values to obtain the desired csv
pair = "BTCUSDT"
since = "1 month ago UTC"

#Connect to the Binance client
client = Client(keys.apiKey, keys.secretKey)

# Get the data from Binance
df = client.get_historical_klines(pair, Client.KLINE_INTERVAL_1MINUTE, since)

# Store the open and close values in a pandas dataframe
real_values = []
for i in df:
    real_values.append([i[1], i[3]])

real_df = pd.DataFrame(real_values, columns=["Real open", "Real close"])

# Normalize the data
normalizer = MinMaxScaler().fit(df)
df = normalizer.transform(df)

# Transform the data to a pandas array
df = pd.DataFrame(df,
                  columns=[
                      "Open time", "Open", "High", "Low", "Close", "Volume",
                      "Close time", "Quote asset volume", "Number of trades",
                      "Taker buy base asset volume",
                      "Taker buy quote asset volume", "Ignore"
                  ])

# Drop useless columns
df.drop(["Open time", "Close time", "Ignore"], axis=1, inplace=True)

#Plot the data
df.plot()

# Add the real open and the real close to df
df = pd.concat([df, real_df], axis=1)

# Remove the last timestep
df = df[:-1]

# Add to the csv file
df.to_csv("datafile/" + pair + ".csv")

#Show the plot
pyplot.show()