from collections import deque
from queue import Queue
class vertex():
    def __init__(self):
        self.visited=False
        self.parent=None
        self.layer=0
def BFS(G,s):
    Q=deque()
    v=0
    for v in range(len(G)):
        v=vertex()
    s=vertex()
    s.visited=True
    Q.append(s)
    while len(Q)>0:
        u=Q[0]
        Q.popleft()
        for v in G[u]:
            if v.visited==False:
                v.layer=u.layer+1
                v.parent=u
                v.visited=True
                Q.append(v)
    def BFS2(G,s):
        Q=Queue()
        d=[-1]*len(G)
        vis=[0]*len(G)
        parent=[None]*len(G)
        d[s]=0
        vis[s]=1
        parent[s]=None
        Q.put(s)
        while not Q.empty():
            u=Q.get()
            for v in G[u]:
                if vis[v]==0:
                    d[v]=d[u]+1
                    parent[v]=u
                    vis[v]=1
                    Q.put(v)
        return d,parent,vis


que=deque([1,2,3,4,5,6,7,8,9,10])
print(que[0])
que.popleft()
print(que[0])
que.popleft()
print(que[0])
Graf=[[0,1,2,3],[490,623,24],[23,123,51]]
for u in Graf[0]:
    print(u)