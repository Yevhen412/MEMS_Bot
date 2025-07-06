from scanner import get_new_dexscreener_pairs
from filter import is_token_sellable
from filter_extended import extended_token_checks
from trader_simulator import simulate_trade
from dotenv import load_dotenv
import os

load_dotenv()

telegram_token = os.getenv("")
telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")

def main():
    print("🚀 Поиск новых токенов...")
    pairs = get_new_dexscreener_pairs()
    for pair in pairs:
        print(f"\n🔍 Проверка: {pair['symbol']} | {pair['age_minutes']} мин | 💧 ${pair['liquidity_usd']}")

        if not is_token_sellable(pair['address']):
            print(f"❌ НЕПРОДАВАЕМЫЙ: {pair['symbol']}")
            continue

        issues = extended_token_checks(pair['address'])
        if issues:
            print("⚠ Обнаружены риски:")
            for issue in issues:
                print(f"   - {issue}")
            continue

        print(f"✅ Симулируем сделку: {pair['symbol']}")
        simulate_trade(pair)

if __name__ == "__main__":
    main()
