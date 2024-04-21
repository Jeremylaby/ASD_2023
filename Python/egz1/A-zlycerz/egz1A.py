from egz1Atesty import runtests
from queue import PriorityQueue
from math import inf
# Stanisław Barycki zlozonosc V^2logV
# pomysł na ten algorytm jest następujący najpierw za pomocą algorytmu dijkstry odnajdujemy 
# najkrótszą droge do wierzchołka pośredniego czyli w tym wypadku do pewnego miasta które planujemy zrabować 
# a następnie szukamy najańszej drogi z tego miasta do końcowego na koniec odejmując liczbe zrabowanych sztabek
# zwracamy  minimum z sumy tych przejść
# oraz z edge casów czyli zrabowania pierwszego miasta i zrabowania ostatniego miasta 
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
    return d[k]
def secound_Dijkstra(G,s,k,V,r):
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
                if relax(d,u,v,c*2+r,par):Q.put((d[v],v))
    return d[k]-V[s]
    
def gold(G,V,s,t,r):
  minn=(inf)
  for i in range (len(G)):
    if i!=s and i!=t:
      minn=min(minn,Dijkstra(G,s,i)+secound_Dijkstra(G,i,t,V,r))
  minn=min(minn,secound_Dijkstra(G,s,t,V,r),Dijkstra(G,s,t)-V[t])
    
  return minn
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )
