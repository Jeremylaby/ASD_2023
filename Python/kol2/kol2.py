from kol2testy import runtests
class Node:
    def __init__(self,value):
        self.parent=self
        self.rank=0
        self.value=value
def find_set(x):
    if x.parent!=x:
        x.parent=find_set(x.parent)
    return x.parent
def union(x,y):
    x=find_set(x)
    y=find_set(y)
    if x.rank > y.rank:
        y.parent=x
    else:
        x.parent=y
        if x.rank == y.rank:
            y.rank+=1
def convert_to_edges(G):
    edges=[]
    edges2=[]
    for i in range(len(G)):
        for j in range(len(G[i])):
            edges.append((i,G[i][j][0],G[i][j][1]))
            if G[i][j][0]>i:
                edges2.append((i,G[i][j][0],G[i][j][1]))

    return edges,edges2
def find_trees(edges,a,n,Vertices,MST,m,M):
    for i in range(a,len(edges)):
        u,v,c=edges[i]
        if  find_set(Vertices[u])!=find_set(Vertices[v]) and (c>m and c<M):
            MST.append(edges[i])
            union(Vertices[u],Vertices[v])
        elif c<m and c>M: return False,MST
    return True,MST
def Kruskal_algo(G,n):
    Vertices=[]
    MST=[]
    edges,edges2=convert_to_edges(G)
    for i in range(len(G)):
        Vertices.append(Node(i))
    flag=False
    a=0
    edges=sorted(edges, key=lambda x: x[2])
    edges2=sorted(edges, key=lambda x: x[2])

    while flag==False and a<(len(edges2)-(n-2)):
        m=edges2[a][2]
        M=edges2[a+(n-2)][2]
        MST=[]
        Vertices2=Vertices
        flag,MST=find_trees(edges,a,n,Vertices2,MST,m,M)
        a+=1
    if flag==True:
        suma=0
        for i in range(len(MST)):
            suma+=MST[i][2]
        return suma
    return None


    
    
def beautree(G):

    return Kruskal_algo(G,len(G))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = True )
