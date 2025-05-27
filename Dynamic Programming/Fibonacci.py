
def compute_fibonacci(num, memo=None):
    if memo is None:
        memo = {}
    if num in memo:
        return memo[num]
    if num == 0:
        memo[0] = 0
    elif num in (1, 2):
        memo[num] = 1
    else:
        memo[num] = compute_fibonacci(num - 1, memo) + compute_fibonacci(num - 2, memo)
    print(memo)
    return memo[num]

print(compute_fibonacci(7))
print(compute_fibonacci(5))
print(compute_fibonacci(10))
