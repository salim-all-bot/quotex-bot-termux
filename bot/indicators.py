import pandas_ta as ta

def calculate_rsi(data, period=14):
    return ta.rsi(data['close'], length=period)

def calculate_macd(data, fast=12, slow=26, signal=9):
    macd = ta.macd(data['close'], fast=fast, slow=slow, signal=signal)
    return macd['MACD_12_26_9'], macd['MACDs_12_26_9'], macd['MACDh_12_26_9']

def calculate_bollinger_bands(data, period=20, std_dev=2):
    bb = ta.bbands(data['close'], length=period, std=std_dev)
    return bb['BBL_20_2.0'], bb['BBM_20_2.0'], bb['BBU_20_2.0']
