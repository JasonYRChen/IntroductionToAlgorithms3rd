def max_profit_prices(prices):
    profit = 0
    low = prices[0]
    for price in prices:
        if price < low:
            low = price
        elif price - low > profit:
            profit = price - low
    return profit


def max_profit_diffs(diffs):
    profit = 0
    current = 0
    for diff in diffs:
        if current + diff > 0:
            current += diff
        else:
            current = 0
        if current > profit:
            profit = current
    return profit


prices = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
diffs = [prices[i]-prices[i-1] for i in range(1, len(prices))]
print(max_profit_prices(prices))
print(max_profit_diffs(diffs))
