# Introduction

Stocksymbol connects to the [StockSymbol API](https://stock-symbols.herokuapp.com/) that I created and provides a list of stock symbols from all major stock exchanges across various regions and markets.

# Quick Start

## Install package

```
pip install stocksymbol
```

## Get an API key

You can register for a free API key [here](https://stock-symbols.herokuapp.com/).

## Symbol list

```
from stocksymbol import StockSymbol

api_key = '<your API key here>'
ss = StockSymbol(api_key)

# get symbol list based on market
symbol_list_us = ss.get_symbol_list(market="US") # "us" or "america" will also work

# get symbol list based on index
symbol_list_spx = ss.get_symbol_list(index="SPX")

# show a list of available market
market_list = ss.market_list

# show a list of available index
index_list = ss.index_list
```

# Further reads
Check out this blog post for a detailed tutorial with output examples and the motivation behind stocksymbol.

