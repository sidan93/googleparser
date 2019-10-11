# About
Module for parsing google search results without access to Google Search API

# Simple Start for home project

1. Install package from pip
```
pip install googleparser
```

2. Use 
```
from googleparser import GoogleParser
print(*['\n' + str(res) for res in GoogleParser().query('bitcoin_price')])
```

Results:
```
#1. Bitcoin Price Chart (BTC) | Coinbase. Link: https://www.coinbase.com/price/bitcoin 
#2. BitcoinAverage: Bitcoin Price Index API & Exchange Rates. Link: https://bitcoinaverage.com/ 
#3. Bitcoin Price - Live Bitcoin Price in USD with No Ads. Link: https://www.bitcoinprice.com/ 
#4. Bitcoin Price Index — Real-time Bitcoin Price Charts — CoinDesk. Link: https://www.coindesk.com/price/bitcoin 
#5. Bitcoin Price Chart Today - Live BTC/USD - Gold Price. Link: https://goldprice.org/ru/cryptocurrency-price/bitcoin-price 
#6. $8,435.00 Bitcoin Price - Blockchain. Link: https://www.blockchain.com/de/prices 
#7. MUST SEE: This Bitcoin Price Action already happened 1:1 in 2016 .... Link: https://www.youtube.com/watch?v=JFo7NcokNPU 
#8. Bitcoin price targets & pivots LIVE STREAM - BTX, LTC & ETH .... Link: https://www.youtube.com/watch?v=87xi-5FRK5M 
#9. BitcoinPrice  DLive. Link: https://dlive.tv/BitcoinPrice
```

## API

### GoogleParser
Class for search links

#### query
Method for search and get results

###### Params
* search_string: str - Query for search

###### Result
* List of GoogleResult

### GoogleResult
Class for result from GooleParser

###### Variable:
* index: int - number of result
* title: str - result title
* link: str - result link
