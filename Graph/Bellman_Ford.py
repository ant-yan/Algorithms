node_map = {
    0: [(1, 5)],
    1: [(2, 20), (5, 30), (6, 60)],
    2: [(3, 10), (4, 75)],
    3: [(2, -15)],
    4: [(9, 100)],
    5: [(4, 25), (6, 5), (8, 50)],
    6: [(7, -50)],
    7: [(8, -10)],
    8: [],
    9: []
}

def BellmanFord(node_map, origin):
  n = len(node_map)
  distance_map = [float('inf') for i in range(n)]
  distance_map[origin] = 0
  affected_nodes = []

  for i in range(n-1):
    for u in node_map:
      for v, w in node_map[u]:
        if distance_map[v] > distance_map[u] + w:
          distance_map[v] = distance_map[u] + w
  dist_1 = distance_map.copy()

  for u in node_map:
    for v, w in node_map[u]:
      if distance_map[v] > distance_map[u] + w:
        distance_map[v] = distance_map[u] + w
        affected_nodes.append(v)
  nodes = [i for i in node_map.keys()]

  for i in nodes:
    print("Shortest path from", origin, "->", i, "is", distance_map[i])
  print("Affected nodes:", affected_nodes)

BellmanFord(node_map, 0)