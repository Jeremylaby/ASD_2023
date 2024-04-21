from queue import PriorityQueue
from math import inf
def Relax_A_B(G,v,u,c,znak,d,par):
    if znak=="B":
        if d[v]>d[u]:
            d[v]=d[u]
            par[v]=u
            return True
        return False
    else: 
        if d[v]>d[u]+c:
            d[v]=d[u]+c
            par[v]=u
            return True
        return False
def Dijkstra_A_B(G,start,meta,znak):
    n=len(G)
    d=[inf]*n
    parent=[None]*n
    d[start]=0
    Q=PriorityQueue()
    Q.put((d[start],start,znak))
    while not Q.empty():
        w,u,znak1=Q.get()
        if w==d[u]:
            for v,cost in G[u]:
                if Relax_A_B(G,v,u,cost,znak1,d,parent):
                    if znak1=="A":
                        Q.put((d[v],v,"B"))
                    else:
                        Q.put((d[v],v,"A"))
    return parent,d
def Bob_Alice(G,start,meta):
    parent,d=Dijkstra_A_B(G,start,meta,"A")
    parent2,d2=Dijkstra_A_B(G,start,meta,"B")
    if d2[meta]<d[meta]: return "B",parent2,d2,meta
    else: return "A",parent,d,meta
Graf=[[(1,50),(2,30),(8,60)],[(0,50),(3,30),(4,20)],[(0,30),(3,10),(4,10),(6,20)],[(1,30),(2,10),(4,50)],
      [(1,20),(2,10),(3,50),(5,70),(7,5)],[(4,70),(6,10),(7,60)],[(2,20),(5,10)],[(4,5),(5,60)],[(0,60)]]


string,parent,d,meta=Bob_Alice(Graf,7,8)
i=meta
print(string)
while i!= None:
    print(d[i],i)
    i=parent[i]
print(inf<1000000)
