# Simple program to pull CryptoData from coinlore and append to personal file on desktop
import os
import requests
import json
import datetime

url = "https://api.coinlore.net/api/tickers/"
response = requests.get(url)
data = response.json()

day=datetime.datetime.now()

if not os.path.exists('C:/Users/12512/Desktop/cryptodata.csv'):
    with open('C:/Users/12512/Desktop/cryptodata.csv', 'w') as f:
        f.write("Ticker Symbol,Ticker Name,Price USD,Volume Over Last 24h,Percent Change Over Last 24h\n")

with open('C:/Users/12512/Desktop/cryptodata.csv', 'a') as f:
    f.write(day.strftime("%c")+"\n")
    for coin in data['data']:
        sentence = (coin['symbol'] + "," + coin['name'] + "," + str(coin['price_usd']) + "," + str(coin['volume24']) + "," + str(coin['percent_change_24h']) + "%\n")
        f.write(sentence)