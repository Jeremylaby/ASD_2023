# Z1 1) Sprawdzenie c zy graf jest dwudzielny BFS
#    2) sprawdzenie spójnych składowych grafu DFS






def dwudzielny(G,start_v):
    colors=[-1]*len(G)
    Q=Queue()
    while not Q.empty():
        v=Q.get()
        for n in G[v]:
            if colors ==-1:
                colors[n]=(colors[v]+1)%2
                Q.put(n)
            else:
                if colors[n]==colors[v]: return False
    return True
def spojny(G,start_v):
    visited=[0]*len(G)
    def DFS(v):
        visited[v]=1
        for u in G[v]:
            if visited[u]: continue
            DFS(u)
    l=0
    for i in range(len(G)):
        if not visited[i]:
            l+=1
            DFS(i)
    return l
#Z2 musimy odciąć sieć komurkową po jednym telefonie
#przechodzimy po grafie BFSem tworzymy tablice tablic i usuwamy wierzchołki od ostatniej tablicy 
def odetnij(G,start_v):


#Z3 Dany jest graf G macież sąsiedztwa Czy istnieje Cykl składający sie z 4 wierzchołków
#a) O(n^4) sprawdzamy każdą trójkę wierzchołków czy są ze sobą połączone 
#b) O(n^3) 1 Rozważamy wszystkie pary wierzchołów x i y i próbujemy do nich dobrać dwa kolejne wierzchołki 
#czyli takie miejsca w tablicy gdzie wiersze  x i y mają 1 na tych samych pozycjach 
def cykl_4(G):
    for i in range (len(G)):
        for j in range(len(G)):
            c=0
            for k in range(len(G)):
                if G[i][k] and G[j][k]:
                    c+=1
                if c>=2:
                    return True
    return False

#Z4 znaleźć uniwersalne wyjście t 
# dla każdego v istnieje krawędź  a v do t 
# t nie posiada krawedzi wychodzacych 
# G - graf  skierowany jako macież sasiedztwa 


#Z5
def spath(G,s,t):
    visited=[0]*len(G)
    parent=[-1]*len(G)
    Q=Queue()
    visited[s]=1
    Q.put(s)
    while Q is not Q.empty():
        u=Q.get()
        for x in G[u]:
            if visited[x]==1: continue
            visited[x]=1
            parent[x]=u
            Q.put(x)
        t=[k]
        while parent[k]!=-1:
            t.append(parent[k])
            k=parent[k]
        return t
#Z6 danaa jest szachownica nxn
#każde pole ma koszt {1,2,3,4,5} znaleźć najtańszą drogę 


#Z7 Malejące krawędzie graf nie skierowany 

#Z8 G=(V,koszt)


