class RiskManager:
    def __init__(self, stake_percentage=2):
        self.stake_percentage = stake_percentage

    def calculate_trade_amount(self, balance):
        return balance * (self.stake_percentage / 100)
