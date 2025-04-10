"""net = {
    'A': ['D'],
    'B': ['D'],
    'C': ['A', 'B'],
    'D': ['visual_net', 'H'],
    'E': ['A', 'D', 'F'],
    'F': ['J', 'K'],
    'visual_net': ['I'],
    'H': ['I', 'J'],
    'I': ['L'],
    'J': ['L', 'M'],
    'K': ['J'],
    'L': [],
    'M': []
}"""

net = {
    'A' : ['B', 'C', 'D'],
    'B' : ['J'],
    'C' : ['F', 'I'],
    'D' : ['E', 'visual_net'],
    'E' : ['K', 'H'],
    'F' : [],
    'visual_net' : [],
    'H' : [],
    'I' : [],
    'J' : [],
    'K' : []
}

def depth_traversal(start_node, seen_nodes, visitednodes, net):
  seen_nodes[start_node] = True
  neighbours = net[start_node]
  for i in neighbours:
    if not seen_nodes[i]:
      depth_traversal(i, seen_nodes, visitednodes, net)
  visitednodes.append(start_node)


def topsort(net):
  n = len(net)
  seen_nodes = {current: False for current in net}
  sorted_output = []

  for start_node in net:
    if seen_nodes[start_node] == False:
      visitednodes = []
      depth_traversal(start_node, seen_nodes, visitednodes, net)
      for nodeId in visitednodes:
        sorted_output.append(nodeId)
  return sorted_output

ordering = topsort(net)
ordering.reverse()
print("Topological ordering: ", ordering)
