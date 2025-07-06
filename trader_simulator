
import time
import random
from telegram_alerts import send_telegram_message

def simulate_trade(token):
    # Вход
    entry_price = random.uniform(0.0000001, 0.0001)
    sell_tax = token.get("sell_tax", 0.05)
    liquidity = token.get("liquidity_usd", 0)
    token_name = token.get("name", "Unknown")
    symbol = token.get("symbol", "???")
    url = token.get("url", "#")

    send_telegram_message(f"🟢 *Покупка*: ${symbol}\n💰 Цена входа: ${entry_price:.10f}\n🔁 Sell tax: {sell_tax*100:.1f}%\n💧 Ликвидность: ${liquidity:,.0f}\n⏳ Ожидание выхода...")

    # Ждём симулированное удержание
    time.sleep(10)  # заменишь на 30-60 сек в бою

    # Выход
    profit_multiplier = random.uniform(1.05, 1.5)
    exit_price = entry_price * profit_multiplier
    net_profit = (exit_price - entry_price * (1 + sell_tax)) / entry_price * 100

    send_telegram_message(f"🔴 *Продажа*: ${symbol}\n📈 Цена выхода: ${exit_price:.10f}\n📊 Прибыль: {net_profit:+.1f}%\n🔗 [Dexscreener]({url})")
