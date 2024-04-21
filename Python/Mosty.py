from math import inf
def bridges(G):
    parent =[None for _ in range(len(G))]
    low=[inf for _ in range(len(G))]
    time_vis=[0 for _ in range(len(G))]
    visited=[0 for _ in range(len(G))]
    Bridges=[]
    for i in range(len(G)):
        if not visited[i]:
            DFS(i,G,parent,low,time_vis,0,visited)
    for i in range(len(G)):
        if time_vis[i]==low[i] and parent[i]!=None: # jeżeli chcemy aby te algorytm wyszukiwał punkty artykulacji
            print(parent[i],i)                      # musimy w tym miejscu dodać warunek że len(G[i])>1 a także stworzyć
            Bridges.append((parent[i],i)) 
    print(time_vis)
    print(low)          #tablice pkt artykulacji

def DFS(s,G,parent,low,time_vis,time,visited):
    time_vis[s]=time
    time+=1
    visited[s]=1
    low[s]=time_vis[s]
    for v in G[s]:
        if not visited[v]:
            parent[v]=s
            DFS(v,G,parent,low,time_vis,time,visited)
            low[s]=min(low[v],low[s])
        elif parent[s]!=v:
            low[s]=min(time_vis[v],low[s])
Graf1=[[1,3],[0,2],[3,4],[0,2,7],[2,5,6],[4,6],[4,5],[3],[9,11],[8,11],[11,12],[8,9,10],[10,13],[12]]
G = [[1, 2],
    [0, 2],
    [0, 1, 3],
    [2, 4, 5, 9],
    [3, 6],
    [3, 6],
    [4, 5, 7, 8],
    [6],
    [6, 9],
    [3, 8]]
bridges(G)

