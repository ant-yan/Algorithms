
def max_earnings(prices):
    result = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            result += prices[i] - prices[i - 1]
    return result

example = [10, 15, 8, 7, 6, 9, 10, 5, 15, 20, 21, 17]
print(max_earnings(example))
