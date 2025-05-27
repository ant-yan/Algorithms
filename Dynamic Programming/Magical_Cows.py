
TOTAL_DAYS = 50
COW_LIMIT = 8
FARMS = 4
VISITS = 4
cows_start = [1, 3, 2, 1]
check_days = [1, 2, 3, 4, 5, 6]

dp_table = [[0] * (COW_LIMIT + 1) for _ in range(TOTAL_DAYS + 1)]

def count_farms(day_matrix, day_index):
    return sum(day_matrix[day_index])

def simulate_growth():
    for idx in range(FARMS):
        dp_table[0][cows_start[idx]] += 1

    for d in range(TOTAL_DAYS):
        for c in range(COW_LIMIT + 1):
            if c <= COW_LIMIT / 2:
                dp_table[d + 1][2 * c] += dp_table[d][c]
            else:
                dp_table[d + 1][c] += 2 * dp_table[d][c]

    print(f"Initial Day: {FARMS}")
    for i, day in enumerate(check_days):
        print(f"Day {i + 1}: {count_farms(dp_table, day)}")

    for d, row in enumerate(dp_table):
        print(f"day{d}", row)

simulate_growth()
