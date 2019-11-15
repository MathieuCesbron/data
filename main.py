from datacreation import Datacreation
import keys

newdata = Datacreation(keys.apiKey, keys.secretKey, "ETHUSDT",
                       "1 day ago UTC")

newdata.uniformalize()