def DFS(G,A,visited,u):
    visited[u]=True
    for v in G[u]:
        if not visited[v]:
            DFS(G,A,visited,v)
    A.append(u) 
def topology_sort(G):
    A=[]
    visited=[False for _ in range(len(G))]
    for i in range(len(G)):
        if not visited[i]:
            DFS(G,A,visited,i)
    A=A[::-1]
    return A
Graf=[[1,2],[2,4],[],[],[3,6],[4],[]]
print(topology_sort(Graf))