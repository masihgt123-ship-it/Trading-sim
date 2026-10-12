prices = [
    100, 101, 103, 102, 104, 106, 105, 107, 109, 108,
    110, 112, 111, 109, 107, 106, 104, 103, 105, 107,
    106, 104, 102, 100, 98, 97, 99, 101, 100, 98,
    96, 95, 97, 99, 101, 103, 102, 104, 106, 105,
    103, 101, 100, 102, 104, 103, 101, 99, 98, 100,
]

WINDOW = 3
start_cash = 1000.0

cash = start_cash
coins = 0.0
buys = 0
sells = 0
history = []
values = []
events = []

for i in range(WINDOW, len(prices)):
    price = prices[i]
    avg = sum(prices[i - WINDOW:i]) / WINDOW
    action = "HOLD"

    if price > avg and coins == 0:
        coins = cash / price
        cash = 0.0
        buys += 1
        action = "BUY"
    elif price < avg and coins > 0:
        cash = coins * price
        coins = 0.0
        sells += 1
        action = "SELL"

    portfolio_value = cash + coins * price
    values.append((i, portfolio_value))
    row = {
        "index": i,
        "price": price,
        "avg": avg,
        "action": action,
        "value": portfolio_value,
    }
    history.append(row)
    if action in ("BUY", "SELL"):
        events.append(row)

if coins > 0:
    final_price = prices[-1]
    cash = coins * final_price
    coins = 0.0
    sells += 1
    events.append({
        "index": len(prices) - 1,
        "price": final_price,
        "avg": None,
        "action": "FINAL CLOSE (SELL)",
        "value": cash,
    })
    values[-1] = (len(prices) - 1, cash)

end_cash = cash
profit = end_cash - start_cash
profit_pct = profit / start_cash * 100

peak_value = start_cash
worst_drop = 0.0
worst_drop_pct = 0.0
for _, value in values:
    if value > peak_value:
        peak_value = value
    drop = peak_value - value
    drop_pct = (drop / peak_value * 100) if peak_value else 0.0
    if drop > worst_drop:
        worst_drop = drop
        worst_drop_pct = drop_pct

first_price = prices[WINDOW]
buy_hold_end = (start_cash / first_price) * prices[-1]
buy_hold_pct = (buy_hold_end - start_cash) / start_cash * 100

print("start:", round(start_cash, 2))
print("end:", round(end_cash, 2))
print("profit:", round(profit, 2), round(profit_pct, 2), "%")
print("trades:", buys + sells, "buys:", buys, "sells:", sells)
print("worst drop:", round(worst_drop, 2), round(worst_drop_pct, 2), "%")
print("buy and hold:", round(buy_hold_end, 2), round(buy_hold_pct, 2), "%")

print("--- first 8 ---")
for row in history[:8]:
    print(
        row["index"],
        row["price"],
        round(row["avg"], 2),
        row["action"],
        round(row["value"], 2),
    )

print("--- buys and sells ---")
for row in events:
    avg = None if row["avg"] is None else round(row["avg"], 2)
    print(row["index"], row["price"], avg, row["action"], round(row["value"], 2))
