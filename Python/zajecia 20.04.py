# 1 Scieżka hamiltona graf a cykliczny skierowany 
def DFS(V,G,vis,A):
    vis[v]=1
    for x in G[v]:
        if vis[v]==0:
            DFS(x,G,vis,A)
    A.append(v)
def hamilton(G):
    A=[]
    vis=[0]*len(G)
    for i in range len(G):
        if vis[v]==0:
            DFS(i,G,vis)
    A.reverse()
    for i in range (len(G)-1):
        U=A[i],V=A[i+1]
        if not V in G[U]: return False
    return True
#dobry początek  kandydat puszczamy DFS 
# ostatni odwiedzony kandydat na dobry początek 
# ten ostatni lub jego silna spolnie składowa jest dobrym poczatkiem
def DFS2(v,G,vis,A,index):
    vis[v]=index
    for x in G[v]:
        if vis[v]==0:
            DFS(x,G,vis,A,index)
    A.append(v)
def good_begin(G):
    vis=[0]*len(G)
    i=0
    last=-1
    for v in range (len(G)):
        if vis[v]==0
            DFS2(v,G,vis,A,index)
            last=v
        for i in range(len(G)):
            vis[i]=False
        DFS(last,G,vis,True)
        for i in range (len(g)):
            if vis[i]==Fasle: return False
        return True
#3 wycieczka po krakowie waga autobusów 
#4 Cykl Eulera wypisanuie
#5 mosty wykrywanie
# 6 państwa jezeli wchodzimy brama polnocna to wychodzimy poludniowa
# mamy jeszcze oazy z kazdej bramny wychodzi jedna droga oazy polaczone jak badz 
# wyznaczenia trasy gońca po wszystkich miastach 
# oazy kolosiebie zamieniamy w jeden wierzcholek a miasta w krawedz euler 




    

