from math import inf
from queue import PriorityQueue
def MST_prim(G,s):
    n=len(G)
    Q=PriorityQueue()
    parent=[None for _ in range(n)]
    visited=[False for _ in range(n)]
    d=[inf for _ in range(n)]
    d[s]=0
    Q.put((d[s],s))
    while not Q.empty():
        val,u=Q.get()
        visited[u]=True
        for v,c in G[u]:
            if d[v]>c and not visited[v]:
                d[v]=c
                parent[v]=u
                Q.put((d[v],v))
    return d,parent
def print_MST(d,parent):
    result = []
    for i in range(len(parent)):
        if parent[i] is not None:
            result.append((i, parent[i], d[i]))
    return result
Graf=[[(1,5),(2,15)],[(0,5),(2,3),(3,16),(4,5)],[(0,15),(1,3),(3,10),(5,18),(6,2)],[(1,16),(2,10),(5,1),(6,3)],[(1,5),(6,3)],[(2,18),(3,1),(6,2)],[(2,2),(3,3),(4,3),(5,2)]]
d,parent=MST_prim(Graf,0)
print(print_MST(d,parent,))
suma=0
for i in range(len(d)):
    suma+=d[i]
print(suma)
