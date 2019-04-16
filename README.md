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
