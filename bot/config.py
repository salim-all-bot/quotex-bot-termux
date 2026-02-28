import os
from dotenv import load_dotenv

load_dotenv()

QUOTEX_EMAIL = os.getenv("QUOTEX_EMAIL")
QUOTEX_PASSWORD = os.getenv("QUOTEX_PASSWORD")
USE_DEMO = os.getenv("USE_DEMO", "true").lower() == "true"
ASSET_NAME = os.getenv("ASSET_NAME", "EUR/USD (OTC)")
TRADE_AMOUNT_PERCENT = float(os.getenv("TRADE_AMOUNT_PERCENT", 2))
TIMEFRAME = int(os.getenv("TIMEFRAME", 60))

RSI_PERIOD = 14
RSI_OVERSOLD = 30
RSI_OVERBOUGHT = 70
MACD_FAST = 12
MACD_SLOW = 26
MACD_SIGNAL = 9
BB_PERIOD = 20
BB_STD = 2
