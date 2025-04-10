node_map = {
    0: [(1, 4), (2, 1)],
    1: [(1, 1)],
    2: [(2, 1), (3, 5)],
    3: [(4, 3)],
    4: []
}


import heapq

n = len(node_map)
origin = 0

def dijkstra(node_map, n, origin):
  seen_nodes = [False for i in range(n)]
  path_map = [-1 for i in range(n)]
  distance_map = [float('inf') for i in range(n)]
  distance_map[origin] = 0
  priority_nodes = []
  heapq.heappush(priority_nodes, (0, origin))

  while priority_nodes:
    minValue, index = heapq.heappop(priority_nodes)

    if seen_nodes[index]:
      continue
    seen_nodes[index] = True

    if distance_map[index] < minValue:
      continue

    for neighbor, weight in node_map[index]:
      if seen_nodes[neighbor]:
        continue
      newDist = distance_map[index] + weight
      if newDist < distance_map[neighbor]:
        distance_map[neighbor] = newDist
        path_map[neighbor] = index
        heapq.heappush(priority_nodes, (newDist, neighbor))


  return path_map, distance_map

path_map, distance_map = dijkstra(node_map, n, origin)
nodes = [i for i in node_map.keys()]

for i in nodes:
  print("Longest path from", origin, "->", i, "is", distance_map[i])