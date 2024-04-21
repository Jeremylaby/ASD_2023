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
    for i in range(len(G)):
        for j in range(len(G[i])):
                edges.append((i,G[i][j][0],G[i][j][1]))
    return edges
def find_trees(edges,a,n,Vertices,MST):
    for i in range(a,len(edges)):
        u,v,c=edges[i]
        if  find_set(Vertices[u])!=find_set(Vertices[v]):
            MST.append(edges[i])
            union(Vertices[u],Vertices[v])
        else: return False,i,MST
    return True,i,MST
def Kruskal_algo(G,n):
    Vertices=[]
    MST=[]
    edges=convert_to_edges(G)
    for i in range(len(G)):
        Vertices.append(Node(i))
    flag=False
    a=0
    edges=sorted(edges, key=lambda x: x[2])
    while flag==False and a<=(len(edges)-(n-1)):
        MST=[]
        Vertices2=Vertices
        flag,a,MST=find_trees(edges,a,n,Vertices2,MST)
    if flag==True:
        suma=0
        for i in range(len(MST)):
            suma+=MST[i]
        return suma
    return None