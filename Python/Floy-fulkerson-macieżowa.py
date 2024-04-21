from collections import deque
from copy import deepcopy
def BFS(s,t):#to do 
    q=deque()
def cap(G,path):
    min1=G[path[0]][path[1]]
    for i in range(1,len(path)-1):
        min1=min(G[path[i]][path[i+1]],min1)
    return min1

def update(G,path):
    w=cap(G,path)
    for i in range(len(path)-1):
        G[path[i]][path[i+1]]-=w
        G[path[i+1]][path[i]]+=w
def floyd_fulkerson(G,s,t): # reprezentacja macierzowa
    flow=0
    G2=deepcopy(G)
    path=BFS(G2,s,t)
    while path:
        flow+=cap(G2,path)
        update(G2,path)
        path=BFS(G2,s,t)
    return flow