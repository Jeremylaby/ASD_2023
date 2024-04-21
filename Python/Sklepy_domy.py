from queue import Queue
from math import inf
def BFS(G,shops):
    Q=Queue()
    d=[inf for _ in range(len(G))]
    int=1
    for s in shops:
        Q=Queue()
        Q.put(s)
        d[s]=0
        visited=[0 for _ in range(len(G))]
        while not Q.empty():
            u=Q.get()
            for v in G[u]:
                if not visited[v] and d[v]>d[u]+1:
                    d[v]=d[u]+1
                    visited[v]=True
                    Q.put(v)
    return d

def Sklepy_domy(roads,shops):
    max_vertex=0
    for i in range(len(roads)):
        max_vertex=max(max_vertex,max(roads[i]))
    G=[[]for _ in range(max_vertex+1)]
    for i,j in roads:
        G[i].append(j)
        G[j].append(i)
    return BFS(G,shops)



roads = [[0, 1], [0, 2], [0, 3], [1, 3], [1, 4], [1, 5], [2, 5], [2, 6], [2, 7], [3, 6], [3, 8],
         [4, 8], [4, 5], [5, 7], [6, 7], [8, 9], [9, 10], [9, 11], [10, 13], [11, 12], [12, 13]]
shops = [2, 3, 9]
roads2=[[0,1],[0,2],[1,3],[2,3],[1,4],[3,5],[4,5],[5,6],[6,7],[7,8],[0,6],[8,12],[12,11],[11,10],[5,9],[3,9],
        [9,10],[10,14],[14,13],[13,15],[14,15],[15,16],[16,17],[17,18],[18,19],[19,16]]
shops2=[3,6]
print(Sklepy_domy(roads,shops))
print(Sklepy_domy(roads2,shops2))