from math import inf
def add_back_edges(G):
    n = len(G)
    counts = [0] * n
    
    for u in range(n):
        counts[u] = len(G[u])
        
    for u in range(n):
        for i in range(counts[u]):
            v = G[u][i][0]
            G[v].append((u, 0))
            
    return counts
    
    
def remove_back_edges(G, counts):
    n = len(G)
    
    for u in range(n):
        while len(G[u]) > counts[u]:
            G[u].pop()
    

def ford_fulkerson(G, s, t):
    n = len(G)
    flow     = [[0] * n for _ in range(n)]
    visited  = [0] * n
    token    = 1
    max_flow = 0
    
    counts = add_back_edges(G)
    
    def dfs(u, min_flow):
        visited[u] = token
        
        if u == t: return min_flow
        
        for v, capacity in G[u]:
            remaining = capacity - flow[u][v]
            if visited[v] != token and remaining > 0:
                new_min_flow = dfs(v, min(remaining, min_flow))
                if new_min_flow:
                    flow[u][v] += new_min_flow
                    flow[v][u] -= new_min_flow
                    return new_min_flow
        return 0
    
    while True:
        path = dfs(s, inf)
        if not path: break
        max_flow += path
        token += 1
        
    remove_back_edges(G, counts)
        
    return max_flow