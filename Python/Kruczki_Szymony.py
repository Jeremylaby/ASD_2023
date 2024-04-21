from math import inf
from queue import Queue
def bridges(G,s):
    parent =[None for _ in range(len(G))]
    low=[inf for _ in range(len(G))]
    time_vis=[0 for _ in range(len(G))]
    visited=[0 for _ in range(len(G))]
    Bridges=[]
    DFS(s,G,parent,low,time_vis,0,visited)
    for i in range(len(G)):
        if time_vis[i]==low[i] and parent[i]!=None:
            Bridges.append((parent[i],i))
    return Bridges,parent,low

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
def mod_BFS(G,sp,sc,trolls):
    n=len(G)
    visited=[False for _ in range(n)]
    Q=Queue()
    sum_of_trolls=0
    visited[sc]=True
    visited[sp]=True
    Q.put(sc)
    sum_of_trolls+=trolls[sc]
    while not Q.empty():
        u=Q.get()
        for v in G[u]:
            if not visited[v]:
                sum_of_trolls+=trolls[v]
                visited[v]=True
                Q.put(v)
    return sum_of_trolls
def dwarves_trolls(G,T,start):
    n=len(G)
    Bridges,parent,low=bridges(G,start)
    if len(Bridges)==0:return False
    max_trolls,corridor=0,0
    for bridge in Bridges:
        curr_sum=mod_BFS(G,bridge[0],bridge[1],T)
        print(curr_sum)
        if curr_sum>max_trolls:
            max_trolls=curr_sum
            corridor=bridge
    return corridor


graph = [[1, 2, 3, 4], [0, 2, 5, 6], [0, 1, 3], [0, 2], [0, 9, 10], [1, 7, 8],
         [1], [5, 8], [5, 7], [4, 10], [4, 9, 11], [10]]
graf2=[[1,2,3],[0,2,3],[0,1,3],[0,1,2]]
trolls = [inf, 2, 8, 7, 17, 4, 13, 3, 12, 3, 1, 11]
trolls2=[inf,5,5,5]
print(dwarves_trolls(graph, trolls, 0))
print(dwarves_trolls(graf2, trolls2, 0))