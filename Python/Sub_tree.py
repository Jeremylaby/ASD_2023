#algorytm liczywielkość wszystkich poddrzew poddrzew dla każdego wierzchołka zaczynając od s 
# na zasadziezmodyfikowanego DFSa zakładamy że drzewo bez dzieci czyli sam korzen ma długość 1 
#jeżeli byśmy chcieli ząłożyć że ma 0 wystarczy zmodyfikować skomentowane linijki
def mod_DFS(G,s,visited,vertices):
    visited[s]=True
    for v in G[s]:
        if len(G[s])==1:#po usunieciu tych linijek oraz
            vertices[s]+=1#
        if not visited[v]:
            mod_DFS(G,v,visited,vertices)
            count=0
            for i in G[s]:
                if visited[i]:count+=1
            if count ==len(G[s]):
                for i in G[s]:
                    vertices[s]+=vertices[i]
                vertices[s]+=1#count-1#i tutaj plus count-1
def sub_tree(edges,s):
    max_v=0
    for i in range(len(edges)):
        max_v=max(max_v,max(edges[i]))
    G=[[] for _ in range(max_v+1)]
    for i,j in edges:
        G[i].append(j)
        G[j].append(i)
    print(G)
    vertices=[0 for _ in range(max_v+1)]
    visited=[False for _ in range(max_v+1)]
    mod_DFS(G,s,visited,vertices)
    #vertices[s]+=1 # i dodać do wierzchołka startowego jeden stopień z uwagi na to że on nie ma korzenia
    return vertices
edges = [[0, 1], [0, 2], [1, 3], [2, 4], [2, 5], [2, 6], [3, 7], [3, 8], [3, 9], [4, 10], [5, 11], [5, 12], [7, 13],
         [7, 14], [8, 15], [9, 16], [9, 17], [11, 18], [11, 19], [11, 20], [12, 21]]

roo=[[4]*3 for _ in range(5)]
print(roo)
print(sub_tree(edges,0))

