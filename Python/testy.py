from queue import PriorityQueue
import math
n=10
graf=[[]*1 for _ in range(n+1)]
graf[1].append((1,0))
print(graf[1])
E = [(0,1, 5),
(1,2,21),
(1,3, 1),
(2,4, 7),
(3,4,13),
(3,5,16),
(4,6, 4),
(5,6, 1)]
S = [ 0, 2, 3 ]
a = 1
b = 5
n = 7
def relax (d,u,v,c,par):
    if d[v]>d[u]+c:
        d[v]=d[u]+c
        par[v]=u
        return True
    else: return False
Graf=[[]*1 for _ in range(n+1)]
for i in S:
    Graf[i].append((n,0))
    Graf[n].append((i,0))
for u,v,c in E:
    Graf[u].append((v,c))
    Graf[v].append((u,c))
for i in range(n+1):
    print(Graf[i])
d=[math.inf for _ in range(n+1)]
d[a]=0
parent=[None for _ in range (n+1) ]
Q=PriorityQueue()
Q.put((d[a],a))
while not Q.empty():
    w,u=Q.get()
    if w == d[u]:
        d[u]=w
        for v,c in Graf[u]:
            if relax(d,u,v,c,parent): Q.put((d[v],v))
print(d[b])