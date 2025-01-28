from binance.client import Client
import time
import json

API_KEY = 'EzcN2gIOcBrfRonU9n0nL5K5R4NXtfVltddog38KRifW3iVXKddR2hEG1CZnaJsa'
API_SECRET = 'HcFFXvxAE0EyMyyR1tqfMbUwwx0DUSIbHO5A9DxQ9eQjIqb3RBGiowBErEEQCxrB'

client = Client(API_KEY,API_SECRET,testnet=True)
account_info = client.get_account()

# print(json.dumps(account_info, indent=1))

ETH = 'ETHUSDT'
BTC = 'BTCUSDT'
def get_current_price(symbol):
    ticker = client.get_symbol_ticker(symbol=symbol)
    return float(ticker['price'])


while True :
    # print(get_current_price(ETH))
    print(get_current_price(BTC))