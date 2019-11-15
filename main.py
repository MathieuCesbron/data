from datacreation import Datacreation
import keys

newdata = Datacreation(keys.apiKey, keys.secretKey, "LTCUSDT",
                       "1 hour ago UTC")

newdata.uniformalize()