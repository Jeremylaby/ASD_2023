from math import inf
def bridges(G):
    parent =[None for _ in range(len(G))]
    low=[inf for _ in range(len(G))]
    time_vis=[0 for _ in range(len(G))]
    visited=[0 for _ in range(len(G))]
    AP=[]
    Bridges=[]
    for i in range(len(G)):
        if not visited[i]:
            DFS(i,G,parent,low,time_vis,0,visited,AP)                                 # jeżeli chcemy aby te algorytm wyszukiwał punkty artykulacji  
    print(AP)
    print(time_vis)
    print(low)                                     #tablice pkt artykulacji

def DFS(s,G,parent,low,time_vis,time,visited,AP):
    time_vis[s]=time
    time+=1
    visited[s]=1
    low[s]=time_vis[s]
    for v in G[s]:
        if not visited[v]:
            parent[v]=s
            time=DFS(v,G,parent,low,time_vis,time,visited,AP)
            low[s]=min(low[v],low[s])
            if parent[s]!=None and low[v]>=time_vis[s]:
                AP.append(s)
        elif parent[s]!=v:
            low[s]=min(time_vis[v],low[s])
    return time




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
Graf1=[[1,3]        #0
       ,[0,2]       #1
       ,[1,3,4]     #2
       ,[0,2,7]     #3
       ,[2,5,6]     #4
       ,[4,6]       #5
       ,[4,5]       #6
       ,[3]         #7
       ,[9,11]      #8
       ,[8,11]      #9
       ,[11,12]     #10
       ,[8,9,10]    #11
       ,[10,13]     #12
       ,[12]]       #13
bridges(G)
bridges(Graf1)