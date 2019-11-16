from datacreation import Datacreation
import keys

newdata = Datacreation(keys.apiKey, keys.secretKey, "BTCUSDT",
                       "1 month ago UTC")

newdata.uniformalize()