
def find_ways(nums, tgt):
    total = sum(nums)
    if tgt > total or (tgt + total) % 2 == 1:
        return False

    goal = (tgt + total) // 2
    dp = [0] * (goal + 1)
    dp[0] = 1

    for num in nums:
        for i in range(goal, num - 1, -1):
            dp[i] += dp[i - num]

    return dp[goal]

print("Possible combinations:", find_ways([1, 1, 1, 1, 1], 3))
