import ccxt
import pandas as pd
import numpy as np
from datetime import datetime
from twilio.rest import Client
from api import account_sid, auth_token, twilio_number, recipients, coins

client = Client(account_sid, auth_token)
binance = ccxt.binance()

windows = [8, 21, 55, 99]
message = ''

for coin in coins:
    try:
        ticker = coin + '/USDT'
        data = binance.fetch_ohlcv(ticker, '1h')
    except:
        ticker = coin + '/BTC'
        data = binance.fetch_ohlcv(ticker, '1h')

    averages = pd.DataFrame()
    df = pd.DataFrame(
        columns=['timestamp','open', 'high', 'low', 'close', 'volume'],
        data=data
    )

    for window in windows:
        averages.loc[:, window] = df['open'].rolling(window=window).mean()
        # averages.loc[:, window] = df['open'].ewm(span=window).mean()

    averages.dropna(inplace=True)
    averages.reset_index(drop=True, inplace=True)
    averages.sort_index(inplace=True)

    daily = averages[-24:]
    averages_crossed = 0

    for avg1 in windows[:-1]:
        for avg2 in windows[windows.index(avg1) + 1:]:
            col = str(avg1) + ' > ' + str(avg2)
            daily.loc[:, col] = daily[avg1] > daily[avg2]
            num_changes = len(daily) - len(daily[daily[col] == True])
            if num_changes > 0:
                averages_crossed += 1

    daily.drop(windows,axis=1, inplace=True)

    sentiment = None
    if averages_crossed == len(list(daily)):
        support_pct = daily.iloc[-1].sum()
        if support_pct == 0: # BEARISH
            sentiment = "BEARISH"
        elif support_pct == len(list(daily)): # BULLISH
            sentiment = "BULLISH"

    if sentiment is not None:
        message += sentiment + ':   ' + ticker + '\n'


# Send the text message
if len(message) > 0:
    print('Signal created')
    for recipient in recipients:
        client.messages.create(
            from_=twilio_number,
            body=message,
            to=recipient
        )
