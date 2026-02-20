from binance.client import Client
import os

class BinanceFuturesClient:
    def __init__(self):
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")

        if not api_key or not api_secret:
            raise ValueError("API Key or Secret not found in environment variables")

        self.client = Client(api_key, api_secret)

         # IMPORTANT: Set Futures Testnet URLs explicitly
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
        self.client.FUTURES_DATA_URL = "https://testnet.binancefuture.com/fapi"