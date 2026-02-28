class TradeExecutor:
    def __init__(self, config):
        self.config = config

    def place_trade(self, trade_type, amount):
        print(f"ট্রেড প্লেস করা হবে: {trade_type} (${amount})")
        return True
