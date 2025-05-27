
def compute_factorial(value, cache=None):
    if cache is None:
        cache = {}
    if value in (0, 1):
        return 1
    if value in cache:
        return cache[value]
    cache[value] = value * compute_factorial(value - 1, cache)
    print(cache)
    return cache[value]

print(compute_factorial(7))
print(compute_factorial(5))
print(compute_factorial(10))
