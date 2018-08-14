#!/usr/bin/env python

import requests

url = "https://quote.coins.ph/v1/markets/BTC-PHP"

headers = {
    'Cache-Control': "no-cache",
    'Postman-Token': "3f791a1b-c1ce-46e2-98ee-6cd4591fcd35"
    }

response = requests.request("GET", url, headers=headers)

print response.text

