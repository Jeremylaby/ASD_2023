# Floyd fulkerson
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
#wiele źródeł wiele ujść łączymy z każdego źródła możemy wypuścić określoną liczbę gazu
#  a w ujściach możemy odebrać określoną ilość gazu żródła łaczymy w jeden wierzchołek 
# krawędziami skierowanymi o wadze takiej jak maksymalna przepustowość źródła nowe źródło ->(waga źródła) stare źródła
# analogicznie z ujściami stare ujścia ->(waga ujścia) nowe ujście
def multi_FF(G,sources,sinks):
    n=len(G)
    G2=deepcopy(G)
    G2.append([0]*(n+2))
    G2.append([0 for _ in range(n+2)])
    for i in range(n):
        G2[i].extend([0,0])
    for u,v in sources:
        G2[n][u]=v
    for u,v in sinks:
        G2[u][n+1]=v
#ile musimy usunąć krawędzi żeby graf był niespójny maksymakny przepływ 
# dla jednego wybranego źródła i dla wszystkich możliwych ujść graf nie ważony nie skierowany

#garf niw ważony dwudzielny łączymy jedną grupę ze źródłem drugą z ujściem krawędziami skierowanymi i puszczamy FF

#maksymalne skojarzenie pomiędzy wierzchołkami drzewa nieskierowany a cykliczny 
# drzewo jest grafem dwudzielnym zmodyfikowany bfs który grupuje nam wierzchołki

#mamy graf skierowany maksymalna liczba ścieżek wierzcholkowo rozłącznych z s do t 
# każdy wierzchołek zamieniamy na 2 z podwójną krawędzią miezy tymi dwoma o wadze 1 i 0 
# reszta krawędź o wadze 1 


# warto

 