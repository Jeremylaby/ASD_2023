from egzP3btesty import runtests 
from queue import PriorityQueue
from math import inf
# pomysł na poniższy algorytm wygląda następująco puszczamy bfsa zaczynając 
# od jakiego kolwiek wierzchołka używając zamiast zwykłej kolejki PriariorityQueue
# na kolejke wrzucamy krotke (-wartość kraswędzi,wierzchołek do kt orego idziemy, poprzedni wierzchołek)
# jeżeli v to jest wierzchołek którego jeszcze nie odwiedziliśmy to do kolejki wrzucamy wszystkie wierzchołki z którymi jest połączony
# oprócz tych które juz odwiedziliśmy wraz z wagą krawędzi które je łaczy 
# jeżeli v to wierzchołek w którym już byliśmy to dodajemy wartość krawędzi(w zasadzie odejmujemy go od sumy)
# na koniec od sumy odejmujemy największą z odrzuconych krawędzi
# w tym zadaniu chodzi o znalezienie największego drzewa rozpinającego graf i największą krawędź z pozostałych  

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
        if not visited[v]:
            visited[v]=True
            parent[v]=prev
            for u,cost in G[v]:
                if not visited[u]:
                    Q.put((-cost,u,v))
        else:
            suma-=val
            maks=min(maks,val)
    #tutaj proszę wpisać własną implementację 
    return suma+maks
runtests ( lufthansa, all_tests=True )