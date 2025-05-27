
# Brute-force O(n^2)
def analyze(prices):
    size = len(prices)
    min_val = min(prices)
    max_val = max(prices)
    if min_val == max_val:
        return 0
    if prices.index(min_val) < prices.index(max_val):
        return max_val - min_val, "Buy at:", prices.index(min_val), "Sell at:", prices.index(max_val)
    else:
        best = 0
        for x in range(size):
            for y in range(x + 1, size):
                if prices[y] - prices[x] > best:
                    best = prices[y] - prices[x]
                    buy, sell = x, y
        return best, "Buy at:", buy, "Sell at:", sell

# Optimized O(n)
def best_trade(prices):
    min_price = prices[0]
    best_gain = 0
    for p in prices[1:]:
        if p > min_price:
            best_gain = max(best_gain, p - min_price)
        else:
            min_price = p
    return best_gain

data = [4, 5, 8, 10, 6, 2, 9, 7, 1, 3, 2]
print(analyze(data))
print(best_trade(data))
