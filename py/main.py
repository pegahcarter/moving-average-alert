import ccxt
import pandas as pd
import numpy as np


key, secret = pd.read_csv('../../api.csv').iloc[0]
x = ccxt.binance({'options': {'adjustForTimeDifference': True}, 'apiKey': key, 'secret': secret})
