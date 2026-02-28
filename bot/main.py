
from flask import Flask, render_template, jsonify, request
import threading
import time
import pandas as pd
import random
from .config import *
from .strategy import TradingStrategy
from .risk_management import RiskManager
from .trade_executor import TradeExecutor

app = Flask(__name__, template_folder='../templates')

# গ্লোবাল ভেরিয়েবল
bot = None
current_signal = {"type": "HOLD", "confidence": 0, "price": 0, "time": ""}

class QuotexBot:
    def __init__(self):
        self.config = config
        self.strategy = TradingStrategy(self.config)
        self.risk_manager = RiskManager(self.config.TRADE_AMOUNT_PERCENT)
        self.executor = TradeExecutor(self.config)
        self.running = False
        self.price_data = pd.DataFrame(columns=['close'])

    def start(self):
        self.running = True
        thread = threading.Thread(target=self._run_loop)
        thread.daemon = True
        thread.start()

    def _run_loop(self):
        while self.running:
            try:
                # সিমুলেটেড মার্কেট ডেটা (API থেকে আনতে হবে বাস্তবে)
                new_price = random.uniform(1.05, 1.15)  # ইউর/ডলার র্যান্ডম
                self.price_data.loc[len(self.price_data)] = new_price
                if len(self.price_data) > 100:
                    self.price_data = self.price_data.iloc[-100:]

                # সিগন্যাল জেনারেট
                if len(self.price_data) > 30:
                    signal, conf = self.strategy.generate_signal(self.price_data)
                    global current_signal
                    current_signal = {
                        "type": signal,
                        "confidence": conf,
                        "price": new_price,
                        "time": time.strftime("%H:%M:%S")
                    }
                time.sleep(5)  # প্রতি ৫ সেকেন্ডে আপডেট
            except Exception as e:
                print(f"Error: {e}")

bot = QuotexBot()

@app.route('/')
def index():
    return render_template('index.html', signal=current_signal)

@app.route('/api/signal')
def api_signal():
    return jsonify(current_signal)

@app.route('/start', methods=['POST'])
def start_bot():
    if not bot.running:
        bot.start()
        return jsonify({"status": "started"})
    return jsonify({"status": "already running"})

@app.route('/stop', methods=['POST'])
def stop_bot():
    bot.running = False
    return jsonify({"status": "stopped"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
