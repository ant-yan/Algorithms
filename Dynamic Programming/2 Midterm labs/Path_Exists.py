
def check_path(node_count, edge_list, start, end):
    net = {i: [] for i in range(node_count)}
    for a, b in edge_list:
        net[a].append(b)
        net[b].append(a)

    to_visit = [start]
    seen = set()

    while to_visit:
        curr = to_visit.pop(0)
        if curr == end:
            return True
        if curr not in seen:
            seen.add(curr)
            to_visit.extend(net[curr])
    return False

edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
print("Path exists:", check_path(6, edges, 0, 5))
print("Path exists:", check_path(6, edges, 3, 5))
