adj_matrix = [[0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
              [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
              [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
              [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
              [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]]



def breadth_scan(adj_matrix, start):
  n = len(adj_matrix)
  seen_nodes = set()
  node_line = [start]
  seen_nodes.add(start)


  while node_line:
    current = node_line.pop(0)
    print(current, end="-->")

    for i in range(n):
      if adj_matrix[current][i] == 1 and i not in seen_nodes:
        seen_nodes.add(i)
        node_line.append(i)


breadth_scan(adj_matrix, 0)
