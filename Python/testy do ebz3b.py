from queue import PriorityQueue
from math import inf
def lufthansa ( G ):
    n=len(G)
    visited=[False for _ in range(n)]
    parent=[None for _ in range(n)]
    Q=PriorityQueue()
    Q.put((0,0,None))
    visited[0]=False
    maks=0
    suma=0
    number=1
    while not Q.empty():
        val,v,prev=Q.get()
        print(val,v,prev)
        if not visited[v]:
            visited[v]=True
            parent[v]=prev
            for u,cost in G[v]:
                if not visited[u]:
                    Q.put((-cost,u,v))
        else:
            print(val)
            suma-=val
            maks=min(maks,val)
        
        
            

    

    #tutaj proszę wpisać własną implementację 
    return suma+maks
G = [
[(1, 15), (2, 5), (3, 10) ],
[(0, 15), (2, 8), (4, 5), (5, 12)],
[(0, 5), (1, 8), (3, 5), (4, 6) ],
[(0, 10), (2, 5), (4, 2), (5, 11)],
[(1, 5), (2, 6), (3, 2), (5, 2) ],
[(1, 12), (4, 2), (3, 11) ] 
]
print("siema",lufthansa(G))