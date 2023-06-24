def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1

def kruskal(graph):
    result = []
    parent = []
    rank = []

    graph = sorted(graph, key=lambda item: item[2])

    for node in range(len(graph)):
        parent.append(node)
        rank.append(0)

    i = 0
    while len(result) < len(graph) - 1:
        u, v, weight = graph[i]
        i += 1
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            result.append([u, v, weight])
            union(parent, rank, x, y)

    return result
