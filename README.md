Carter Carlson

### Concept
Technical analysis still plays a big role in price movement within the cryptocurrency world.  This repo takes advantage of moving averages and sends text notifications if the moving average of a price has strong support or strong resistance.

For now, we're utilizing 1-hour price intervals and the **8, 21, 55, and 99** moving averages.  Here's the basic logic:
* Compare each set of moving averages
  * i.e. `[[8, 21], [8,55], [8, 99], [21, 55], [21, 99], [55, 99]]`
* Compare the two averages from the last 24 hours
* Over the 24h interval, find the higher average for each pair
* If the higher moving average changes at least once for every pair, the averages have crossed
* Take the moving average for the most-recent price
* If 8 > 21 > 55 > 99 or 8 < 21 < 55 < 99 (referring to the moving average $), we should see strong support or resistance
* Send an SMS for coins matching the criteria above, labeling them as bullish or bearish

### Setup
* [Create a twilio account and phone #](https://www.twilio.com/login)
* `git clone https://github.com/carlfarterson/TA_signal.git`
* `cd TA_signal`
* `pip install -r Requirements.txt`
* Create a file **py/api.py** and paste the following with your information:
```python
account_sid = 'AC.............................'
auth_token = '................................'
twilio_number = '+1.........'
recipients = ['+1..........', '+1..........']
coins = ['BTC', 'ETH', ...]
```
* Note: keep recipients and coins as a list, even if there's only 1 recipient/coin

### Laundry list
* Backtest different moving average periods
* Backtest different types of moving averages (expontential, weighted)
* Add BTC moving average as a factor (as the market is heavily correlated with BTC price movement)
* Add indicators for sudden price volatility/volume changes
