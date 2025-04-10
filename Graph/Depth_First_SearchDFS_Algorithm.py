net = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

n = len(net)
seen_nodes = [False for i in range(n)]
sorted_output = []


def depth_traversal(start_node):
  if seen_nodes[start_node]:
    return
  seen_nodes[start_node] = True
  neighbours = net[start_node]
  for i in range(n):
    if neighbours[i] == 1:
      depth_traversal(i)
  sorted_output.append(start_node)
  seen_nodes[start_node] = True
  return sorted_output

sorted_output = depth_traversal(0)
sorted_output.reverse()

for i in range(len(sorted_output)):
  if i != len(sorted_output) - 1:
    print(sorted_output[i], end="-->")
  elif i == len(sorted_output) - 1:
    print(sorted_output[i])