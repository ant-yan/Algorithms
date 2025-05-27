
num_items = 5
bag_capacity = 7

item_info = {
    '1': [2, 3],
    '2': [2, 1],
    '3': [4, 3],
    '4': [5, 4],
    '5': [3, 2]
}

dp_matrix = [[0] * (bag_capacity + 1) for _ in range(num_items + 1)]

def knapsack_solver(dp_matrix, num_items, bag_capacity, item_info):
    for i in range(1, num_items + 1):
        for item_id, (val, wt) in item_info.items():
            if str(i) == item_id:
                dp_matrix[i][:wt] = dp_matrix[i - 1][:wt]
                for j in range(wt, bag_capacity + 1):
                    dp_matrix[i][j] = max(dp_matrix[i - 1][j], dp_matrix[i - 1][j - wt] + val)
    return dp_matrix

result_matrix = knapsack_solver(dp_matrix, num_items, bag_capacity, item_info)

for idx, row in enumerate(result_matrix):
    print(f"Item{idx}", row)

selected = []
remaining_capacity = bag_capacity
for i in range(num_items, 0, -1):
    if dp_matrix[i][remaining_capacity] != dp_matrix[i - 1][remaining_capacity]:
        selected.append(i)
        remaining_capacity -= item_info[str(i)][1]

print("Selected items:", selected)
