from queue import PriorityQueue
from math import inf
def Prim(G):
    n = len(G)
    parents   = [None for _ in range(n)]
    d   = [inf for _ in range(n)]
    visited = [False for _ in range(n)]
    queue = PriorityQueue()
    queue.put((0, 0)) 
    
    while not queue.empty():
        value, u = queue.get()
        if not visited[u]:
            visited[u] = True
            for v, cost in G[u]:
                if not visited[v] and cost < d[v]:
                    parents[v] = u
                    d[v] = cost
                    queue.put((cost, v))

    return parents, d


def get_MST(G):
    parents, d = Prim(G)
    n = len(G)
    G = [[] for _ in range(n)]
    for u in range(n):
        if parents[u] != None:
            G[parents[u]].append((u, d[u]))
            G[u].append((parents[u], d[u]))
    return G
def undirected_weighted_graph_list(E):
    # Find a number of vertices
    n = 0
    for e in E:
        n = max(n, e[0], e[1])
    n += 1
    # Create a graph
    G = [[] for _ in range(n)]
    for e in E:
        G[e[0]].append((e[1], e[2]))
        G[e[1]].append((e[0], e[2]))
    return G
G = [[(1, 1), (5, 12)], [(0, 1), (2, 5), (5, 7)], [(1, 5), (3, 3000), (5, 6), (4, 4)], [(2, 3000), (4, 9)], [(5, 8), (2, 4), (3, 9)], [(0, 12), (1, 7), (2, 6), (4, 8)]]
print(G)
print(Prim(G))
print()
print(get_MST(G))