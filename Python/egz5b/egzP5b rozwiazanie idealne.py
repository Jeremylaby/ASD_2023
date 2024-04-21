from egzP5btesty import runtests 
from math import inf
def articulation_points(G):
    parent =[None for _ in range(len(G))]
    low=[inf for _ in range(len(G))]
    time_vis=[None for _ in range(len(G))]
    visited=[0 for _ in range(len(G))]
    ART=[False for _ in range(len(G))]
    Bridges=[]
    for i in range(len(G)):
        if not visited[i]:
            if DFS(i,G,parent,low,time_vis,0,visited,ART)==1:
                ART[i]=False
        
    
    suma=0
    for i in range(len(G)):
        if ART[i]==1:
            suma+=1
    return suma
def DFS(s,G,parent,low,time_vis,time,visited,ART):
    time_vis[s]=time
    time+=1
    children=0
    visited[s]=True
    low[s]=time_vis[s]
    for v in G[s]:
        if time_vis[v] is None:
            children+=1
            parent[v]=s
            DFS(v,G,parent,low,time_vis,time,visited,ART)
            if low[v]==time_vis[s]:
                ART[s]=True
            low[s]=min(low[v],low[s])
        else:
            low[s]=min(time_vis[v],low[s])
    return children
def koleje ( B ):
    n=0
    for i in range(len(B)):
        n=max(n,B[i][0],B[i][1])
        if B[i][0]>B[i][1]:
            B[i]=(B[i][1],B[i][0])
    Graf=[[] for _ in range(n+1)]
    B.sort(key=lambda x:(x[0],x[1]))
    last=(0,0)
    for i in range(len(B)):
        if last!=B[i]:
            Graf[B[i][0]].append(B[i][1])
            Graf[B[i][1]].append(B[i][0])
            last=B[i]
            
    #tutaj proszę wpisać własną implementację
    return articulation_points(Graf)
runtests ( koleje, all_tests=True )