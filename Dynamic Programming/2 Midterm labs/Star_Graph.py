
def build_matrix(edge_list, size):
    mat = [[0] * size for _ in range(size)]
    for a, b in edge_list:
        mat[a][b] = mat[b][a] = 1
    return mat

def identify_star(mat):
    core = []
    leaf = []
    for i, row in enumerate(mat):
        links = sum(row)
        if links == len(mat) - 1:
            core.append(i)
        elif links == 1:
            leaf.append(i)
        else:
            return "Not a star graph!"
    return "Center:", core, "Edges:", leaf

n = 6
edges = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5)]
g = build_matrix(edges, n)
for r in g: print(r)
print(identify_star(g))
