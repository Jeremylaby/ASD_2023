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
            if i<G[i][j][0]:
                edges2.append((i,G[i][j][0],G[i][j][1]))
    return edges,edges2
def partition(A,p,r):
    x=A[r][2]
    i=p-1
    for j in range(p,r):
        if A[j][2]<=x:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]  
    return i+1
def QS2(A,p,r):
    while p<r:
        q=partition(A,p,r)
        if q-p>r-q:
            QS2(A,p,q-1)
            p=q+1
        else:
            QS2(A,q+1,r)
            r=q-1
    return
def Kruskal_algo(G):
    Vertices=[]
    MST=[]
    edges,edges2=convert_to_edges(G)
    for i in range(len(G)):
        Vertices.append(Node(i))
    edges=sorted(edges, key=lambda x: x[2])
    edges2=sorted(edges2, key=lambda x: x[2])
    print(edges)
    print(edges2)
    for i in range(len(edges)):
        u,v,c=edges[i]
        if  find_set(Vertices[u])!=find_set(Vertices[v]):
            MST.append(edges[i])
            union(Vertices[u],Vertices[v])
    return MST
    
graph = [[(1, 7), (2, 8), (3, 3), (4, 2)],
         [(0, 7), (2, 1)],
         [(0, 8), (1, 1), (3, 12), (5, 4)],
         [(0, 3), (2, 12), (5, 6)],
         [(0, 2), (5, 5)],
         [(2, 4), (3, 6), (4, 5)]]
print(Kruskal_algo(graph))