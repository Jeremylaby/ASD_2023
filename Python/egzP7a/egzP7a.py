from egzP7atesty import runtests 
def add_back_edges(G):
    n = len(G)
    counts = [0] * n  # Numbers of edges in an initial graph (before modification)
    
    for u in range(n):
        counts[u] = len(G[u])
        
    for u in range(n):
        for i in range(counts[u]):
            v = G[u][i][0]
            G[v].append((u, 0))  # Add an edge with no weight
            
    return counts
    
    
def remove_back_edges(G, counts):
    n = len(G)
    
    for u in range(n):
        while len(G[u]) > counts[u]:
            G[u].pop()
    

def ford_fulkerson(G: 'graph represented by adjacency lists', s: 'source vertex', t: 'target vertex'):
    n = len(G)
    inf = float('inf')
    flow     = [[0] * n for _ in range(n)]
    visited  = [0] * n
    token    = 1  # Number of iteration to check which vertices have been visited
    max_flow = 0
    
    counts = add_back_edges(G)
    
    def dfs(u, bottleneck):
        visited[u] = token
        
        if u == t: return bottleneck
        
        for v, capacity in G[u]:
            remaining = capacity - flow[u][v]
            if visited[v] != token and remaining > 0:
                new_bottleneck = dfs(v, min(remaining, bottleneck))
                if new_bottleneck:
                    flow[u][v] += new_bottleneck
                    flow[v][u] -= new_bottleneck
                    return new_bottleneck
        return 0
    
    while True:
        increase = dfs(s, inf)
        if not increase: break
        max_flow += increase
        token += 1
        
    remove_back_edges(G, counts)
        
    return max_flow
def akademik( T ):
    n=len(T)*2+2
    start=len(T)*2
    koniec=len(T)*2+1
    Graf=[[]*n for _ in range(n)]
    puste=0
    for i in range(len(T)):
        Graf[start].append((i,1))
        Graf[i+len(T)].append((koniec,1))
        if T[i]==(None,None,None):
            puste+=1
        for j in range(3):
            if T[i][j]!=None:
                Graf[i].append((len(T)+T[i][j],1))
    return len(T)-puste-ford_fulkerson(Graf,start,koniec)

runtests ( akademik )