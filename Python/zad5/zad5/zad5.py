from zad5testy import runtests
from queue import PriorityQueue
from math import inf
#Stanisław barycki 
#Algorytm działa następująco najpierw łączymy wrzystkie wierchołki wokół osobliwości z wierchołkiem na końcu listy sąsiedztwa
# potem resztę tablicy przekształcamy w listę sąsiedztwa
#jeżeli po takim przekształceniu len(Gtaf[b])==0 to nie istnieje droga do b 
# jeżeli nie to szukamy najkrótszej drogi za pomocą algorytmu dijkstry
# złożoność len(S)+E+Elog(V)
def relax (d,u,v,c,par):
    if d[v]>d[u]+c:
        d[v]=d[u]+c
        par[v]=u
        return True
    else: return False
def spacetravel( n, E, S, a, b ):
    Graf=[[]*1 for _ in range(n+1)]
    for i in S:
        Graf[i].append((n,0))
        Graf[n].append((i,0))
    for u,v,c in E:
        Graf[u].append((v,c))
        Graf[v].append((u,c))
    if len(Graf[b])==0: return None
    d=[inf for _ in range(n+1)]
    d[a]=0
    parent=[None for _ in range(n+1)]
    Q=PriorityQueue()
    Q.put((d[a],a))
    while not Q.empty():
        w,u=Q.get()
        if w == d[u]:
            d[u]=w
            for v,c in Graf[u]:
                if relax(d,u,v,c,parent): Q.put((d[v],v))
    if d[b]==inf:return None


    
    # tu prosze wpisac wlasna implementacje
    return d[b]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True)