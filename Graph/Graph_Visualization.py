import matplotlib.pyplot as plt
import networkx as nx

visual_net = nx.Graph()
visual_net.add_edge("a", "b", weight = 0.6)
visual_net.add_edge("a", "c", weight = 0.2)
visual_net.add_edge("c", "d", weight = 0.1)
visual_net.add_edge("c", "e", weight = 0.7)
visual_net.add_edge("c", "f", weight = 0.9)
visual_net.add_edge("a", "d", weight = 0.3)

elarge = [(u, v) for (u, v, d) in visual_net.edges(data=True) if d["weight"] > 0.5]
esmall = [(u, v) for (u, v, d) in visual_net.edges(data=True) if d["weight"] <= 0.5]

pos = nx.spring_layout(visual_net, seed = 7)
nx.draw_networkx_nodes(visual_net, pos, alpha = 0.7, node_size = 1000)
nx.draw_networkx_edges(visual_net, pos, edgelist = elarge, width = 5, alpha = 0.2, edge_color = "r")
nx.draw_networkx_edges(visual_net, pos, edgelist = esmall, width = 5, alpha = 0.5, edge_color = "b", style = "dashed")

nx.draw_networkx_labels(visual_net, pos, font_size = 20, font_family = "sans-serif")
edge_labels = nx.get_edge_attributes(visual_net, "weight")
nx.draw_networkx_edge_labels(visual_net, pos, edge_labels = edge_labels)
ax = plt.gca()
ax.margins(0.08)
plt.tight_layout()

plt.axis("off")
plt.show()