from binance.client import Client
from .config import API_KEY, API_SECRET


from binance.client import Client
from .config import API_KEY, API_SECRET


class BinanceClient:
    def __init__(self):
        self.client = Client(API_KEY, API_SECRET)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def get_client(self):
        return self.client