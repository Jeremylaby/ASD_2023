from zad6testy import runtests
from math import inf
from queue import Queue
from collections import deque
#Stanisław Barycki Algorytm działa następująco
#najpierw tworzę nową listę sąsiedztwa która od 0 do n-1 miejsca( n = len(m))ma wpisaną wartość
# n*2 (tworze krawędzie między tymi wierzchołkami a wierczhołkiem n*2)
#następnie przepisuje listę M 
#oraz dodaje 2 nowe wierzchołki źródło i ujśćie następnie 
# korzystam ze zmodyfikowanego FFa który przy pomocy BFSa szuka ścieżki z s do t 
# jeżeli trafi do t to zwiększa max flowa o 1 i modyfikuje graf 
#usuwając odpowiednie krawędzie i dodając nowe 


def BFS(G,s,t,parent):
    Q=deque()
    vis=[False]*len(G)
    vis[s]=True
    Q.append(s)
    while len(Q)>0:
        u=Q.popleft()
        for v in G[u]:
            if vis[v]==0:
                parent[v]=u
                vis[v]=True
                if v==t: return True
                Q.appendleft(v)
    return vis[t]
def modificated_ff(G, s, t):
    parent=[None for _ in range(len(G))]
    flow = 0
    while BFS(G, s, t, parent):
        flow += 1
        v = t
        
        while v != s:
            u = parent[v]
            G[u].remove(v)
            G[v].append(u)
            v = parent[v]
    return flow
def binworker( M ):
    
    n=len(M)
    G2=[[n*2] for _ in range(n)]
    for i in range(n):
        G2.append(M[i])
    G2.append([])
    G2.append([])
    for i in range(n):
        G2[2*n+1].append(i+n)
    flow=modificated_ff(G2,n*2+1,n*2)

    return flow

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = True )
