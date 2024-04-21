from math import inf
from queue import PriorityQueue,Queue
from math import sqrt   
def distance(koord1,koord2):
    x=abs(koord2[0]-koord1[0])
    y=abs(koord2[1]-koord1[1])
    return sqrt(x**2+y**2)
def relax(d,u,v,c,parent):
    if d[v]>d[u]+c:
        d[v]=d[u]+c
        parent[v]=u
        return True
    return False
def upo_Dijkstra(d,G,start,n,parent):
    d[start]=0
    Q=PriorityQueue()
    Q.put((d[start],start))
    while not Q.empty():
        val,u=Q.get()
        if val==d[u]:
            for v,c in G[u]:
                if relax(d,u,v,c,parent): Q.put((d[v],v))
                if v==n-1:
                    return d,parent
    return d,parent
def Henry_plywak(points_list,Z,start):
    n=len(points_list)
    d=[inf for _ in range(n)]
    G=[[]*n for _ in range(n)]
    parent=[None for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i!=j:
                dist=distance(points_list[i],points_list[j])
                if dist<=Z:
                    G[i].append((j,1))
                elif dist>Z and dist<=2*Z:
                    G[i].append((j,2))
    d,parent=upo_Dijkstra(d,G,start,len(points_list),parent)
    if d[-1]==inf: return None
    else:
        i=len(points_list)-1
        while i!=None:
            print(points_list[i],end=" ")
            i=parent[i]
        print()
        return d[-1]



def Henry_plywak_ale_to_BFS(L,Z,start):
    n=len(L)
    d=[inf for _ in range(n)]
    G=[[]*n for _ in range(n)]
    visited=[False for _ in range(n)]
    parent=[None for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i!=j:
                dist=distance(L[i],L[j])
                if dist<=Z:
                    G[i].append((j,1))
                elif dist>Z and dist<=2*Z:
                    G[i].append((j,2))
    Q=Queue()
    d[start]=0
    Q.put((1,start))
    visited[start]=True
    while not Q.empty():
        c,u =Q.get()
        while c==2:
            Q.put((1,u))
            c,u=Q.get()
        for v,val in G[u]:
            if not visited[v]:
                d[v]=d[u]+val
                visited[v]=True
                parent[v]=u
                Q.put((val,v))
    if d[-1]!=inf:
        j=len(L)-1
        while j  != None:
            print(L[j],end=" ")
            j=parent[j]
        print()
        return d[-1]
    return False


def count_distance(point1, point2):
    x = abs(point1[0] - point2[0])
    y = abs(point1[1] - point2[1])
    return sqrt(x ** 2 + y ** 2)


def the_sailr_Henry(W, Z, start):
    graph = [[] for _ in range(len(W))]
    for i in range(len(W)):
        for j in range(len(W)):
            if i != j:
                distance = count_distance(W[i], W[j])
                if distance <= Z:
                    graph[i].append([j, 1])
                elif distance > Z and distance <= 2 * Z:
                    graph[i].append([j, 2])
    queue = Queue()
    queue.put([start, 0])
    visited = [False] * len(graph)
    visited[start] = True
    parents = [-1] * len(W)
    DP = [inf] * len(W)
    DP[start] = 0
    while not queue.empty():
        u, dist = queue.get()
        if dist == 2:
            while dist == 2:
                dist -= 1
                queue.put((u, dist))
                u, dist = queue.get()
        for v in graph[u]:
            if not visited[v[0]]:
                parents[v[0]] = u
                if v[1] == 1:
                    DP[v[0]] = min(DP[v[0]], DP[parents[v[0]]]) + 1
                else:
                    DP[v[0]] = min(DP[v[0]], DP[parents[v[0]]]) + 2
                visited[v[0]] = True
                queue.put(v)
    if DP[-1] != inf:
        i = len(parents) - 1
        while i != -1:
            print(W[i], end=" ")
            i = parents[i]
        print()
        return DP[-1]
    return False

Z = 2
W = [(0, 0), (0, 1), (2, 1), (1, 3), (2, 5), (3, 2), (5, 2), (4, 4), (3, 4), (4, 1), (2, 4), (5, 5)]
start=1
print(Henry_plywak(W,Z,start))
print(the_sailr_Henry(W, Z, start))
print(Henry_plywak_ale_to_BFS(W,Z,start))
