from math import inf
from queue import PriorityQueue
def relax (u,d,v,c,par):
    if d[v]>d[u]+c:
        d[v]=d[u]+c
        par[v]=u
        return True
    else: return False

def Dijkstra(G,a):
    n=len(G)
    d=[inf for _ in range(n)]
    d[a]=0
    parent=[None for _ in range (n) ]
    Q=PriorityQueue()
    Q.put(d[a],a)
    while Q:
        w,u=Q.get()
        if w == d[u]:
            d[u]=w
            for v,c in G[u]:
                if relax(Q,d,u,v,c,parent): Q.put((d[v]),v)

    return parent,d

# najkrótsze ścieżki w DAGu ważona 
#wierzchołek któryś w topologi
def topolog_sort(G)
def Path_dag(G,s):
    v=topology_sort(G)
    d=[inf]*len(G)
    d[s]=0
    parent=[-1]*len(G)
    for i in v:
        for x,val in G[i]:
            relax(i,d,x,val,parent)
    return d,parent
#odwrucenie tablicy T[::-1]
def print_path_rek(parent,start,u):
    if u!=start:
        print_path_rek(parent,start,parent[u])
    print(u)
def print_path(parent,start,u):
    T=[]
    while u!=None:
        T.appedn(u)
        u=parent[u]
    for i in range(len(T)-1,-1,-1):
        print(T[i])
# najkrótsza droga iloczyny wag krawędzi dikstra tylko że dodajemy logarytmy z wag 
#belman ford relaksujemy każdą krawędź k razy jest odporny na minusy    
#droga pomiędzy dwoma miastami tak że alice jedzie jak najkrótszą drogę bob i alice zmieniają sie po każdym mieście 
# wskazówka wkładamy do kolejki krotki (val,wierzchołek,"A"lub"B")i jeżeli jedzie bob to nie wydłużamy drogi
#startujemy dwa razy dajkstre raz zaczyna Alice raz Bob
# drugi sposób modyfikujemy graf w taki sposób że rozmnażamy wierzchołki tak że dodajemy krawędzie waga zero stara waga


# mamy kantor wymieniamy pieniądze i chcemy znaleźć czy można zarobić belman ford jeżeli istnieje cykl o ujemnej wadze to zarobiliśmy 
# wpsujemy do tablicy logarytmy z wymian 
def Relax(par,d,i,j,G):
    if d[j]>d[i]+G[j][k]:
        d[j]=d[i]+G[j][k]
        par[j]=i
        return True
    return False

def Belman_Ford(G,v):# dla macierzy sąsiedztwa 
    n=len(G)
    d=[inf]*n
    parent=[None]*n
    d[v]=0
    for i in range (n):
        B=False
        for j in range (n):
            for k in range(n):
                if G[j][k]:
                    B|=Relax(parent,d,j,k,G)
        if i ==n-1 and B: return d,parent,False # sprawdzamy czy jest ujemny cykl gdzieś w grafie 
































    



