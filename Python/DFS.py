def DFS_rek(G,visited,parent,time,curr_time,u):
    time[u]=curr_time
    curr_time+=1
    visited[u]=True
    for v in G[u]:
        if not visited[v]:
            parent[v]=u
            curr_time=DFS_rek(G,visited,parent,time,curr_time,v)
    return curr_time
def DFS(G):
    n=len(G)
    visited=[False for _ in range(n)]
    parent=[None for _ in range(n)]
    time=[0 for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            DFS_rek(G,visited,parent,time,0,i)
    return parent,time

G=[ [1, 2, 8],
    [4, 5, 7],
    [9],
    [0, 10, 11],
    [13],
    [6, 7, 13],
    [],
    [8],
    [9],
    [],
    [9, 11],
    [],
    [0, 3],
    [12]]
print(DFS(G))
