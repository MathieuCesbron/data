from datacreation import Datacreation
import keys

newdata = Datacreation(keys.apiKey, keys.secretKey, "LTCUSDT",
                       "1 week ago UTC")

newdata.uniformalize()