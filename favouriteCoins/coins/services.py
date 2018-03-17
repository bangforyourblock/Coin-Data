import json

import requests


def get_coins(maxcoins):
    url = 'https://api.coinmarketcap.com/v1/ticker/?limit=10'
    r = requests.get(url)
    coin_list = {}
    coin_list = r.json()
    return coin_list
