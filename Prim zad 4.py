import heapq

def prim(graph):
    n = len(graph)
    visited = [False] * n
    min_heap = []
    mst = []

    def process_vertex(v):
        visited[v] = True
        for u, weight in graph[v]:
            if not visited[u]:
                heapq.heappush(min_heap, (weight, u, v))

    start_vertex = 0  # Wybierz dowolny wierzchołek startowy
    process_vertex(start_vertex)

    while min_heap:
        weight, u, v = heapq.heappop(min_heap)
        if not visited[u]:
            mst.append((v, u, weight))
            process_vertex(u)

    return mst

# Przykładowe użycie
graph = [
    [(1, 4), (7, 8)],
    [(0, 4), (7, 11), (2, 8)],
    [(1, 8), (8, 2), (5, 4)],
    [(4, 9), (5, 14)],
    [(3, 9), (5, 10)],
    [(2, 4), (3, 14), (4, 10), (6, 2)],
    [(5, 2), (7, 1), (8, 6)],
    [(0, 8), (1, 11), (6, 1), (8, 7)],
    [(2, 2), (6, 6), (7, 7)]
]

minimum_spanning_tree = prim(graph)
print(minimum_spanning_tree)
