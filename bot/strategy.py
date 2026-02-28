import pandas as pd
from .indicators import calculate_rsi, calculate_macd, calculate_bollinger_bands

class TradingStrategy:
    def __init__(self, config):
        self.config = config

    def generate_signal(self, data):
        rsi = calculate_rsi(data, self.config.RSI_PERIOD)
        macd_line, signal_line, hist = calculate_macd(data, self.config.MACD_FAST, self.config.MACD_SLOW, self.config.MACD_SIGNAL)
        lower, mid, upper = calculate_bollinger_bands(data, self.config.BB_PERIOD, self.config.BB_STD)

        current_price = data['close'].iloc[-1]
        current_rsi = rsi.iloc[-1]
        current_macd = macd_line.iloc[-1]
        current_signal = signal_line.iloc[-1]
        prev_macd = macd_line.iloc[-2] if len(macd_line) > 1 else current_macd
        prev_signal = signal_line.iloc[-2] if len(signal_line) > 1 else current_signal

        current_lower = lower.iloc[-1]
        current_upper = upper.iloc[-1]

        # Buy signal
        if current_rsi < self.config.RSI_OVERSOLD and current_macd > current_signal and prev_macd <= prev_signal and current_price <= current_lower:
            return "BUY", 90
        # Sell signal
        elif current_rsi > self.config.RSI_OVERBOUGHT and current_macd < current_signal and prev_macd >= prev_signal and current_price >= current_upper:
            return "SELL", 90
        else:
            return "HOLD", 0
