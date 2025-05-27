
def min_jumps(nums):
    if len(nums) == 1:
        return 0
    max_reach = jumps = curr_end = 0
    trace = []

    for i in range(len(nums) - 1):
        max_reach = max(max_reach, i + nums[i])
        if i == curr_end:
            jumps += 1
            curr_end = max_reach
            trace.append(nums[i])
            if curr_end >= len(nums) - 1:
                break

    print(" -> ".join(map(str, trace)))
    return jumps

arr = [2, 4, 3, 1, 4, 5, 3, 2, 1, 5, 4, 3]
print("Steps needed:", min_jumps(arr))
