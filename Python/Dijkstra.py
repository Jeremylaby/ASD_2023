from queue import PriorityQueue
from math import inf

def relax(d,u,v,c,par):
    if d[v]>d[u]+c:
        d[v]=d[u]+c
        par[v]=u
        return True
    else: return False
def Dijkstra(G,s,k):
    n=len(G)
    d=[inf for _ in range(n)]
    par=[None for _ in range(n)]
    d[s]=0
    Q=PriorityQueue()
    Q.put((d[s],s))
    while not Q.empty():
        val,u=Q.get()
        if val==d[u]:
            for v,c in G[u]:
                if relax(d,u,v,c,par):Q.put((d[v],v))
    return d[k],par,d

Graf=[[(1,5),(2,6),(3,10)],[(0,5),(2,4),(6,20)],[(0,6),(1,4),(4,10)],[(0,10),(6,5)],[(2,10),(5,20),(6,8)],[(4,20)],[(1,20),(3,5),(4,8)]]
val,par,d=Dijkstra(Graf,0,6)
print(val)