#!/usr/bin/env python
import requests
import json

url = "https://quote.coins.ph/v1/markets/BTC-PHP"

headers = {
    'Cache-Control': "no-cache",
    'Postman-Token': "3f791a1b-c1ce-46e2-98ee-6cd4591fcd35"
    }

response = requests.request("GET", url, headers=headers)

print response.text

data = json.loads(response.text)
market = data['market']
buy = market.get('ask')
sell = market.get('bid')

print "Buy bitcoin at:", buy
print "Sell bitcoin at:",  sell


