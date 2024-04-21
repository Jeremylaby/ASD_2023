def DFS(v,G,A,vis):
    vis[v]=1
    for u in G[v]:
        if not vis[u]:
            DFS(u,G,A,vis)
    A.append(v)
def good_begin(G):
    vis=[0]*len(G)
    A=[]
    last=-1
    for v in range (len(G)):
        if not vis[v]:
            DFS(v,G,A,vis)
            last=v
    for i in range (len(G)):
        vis[i]=0
    DFS(last,G,A,vis)
    for i in range (len(G)):
        if vis[i]==0: return False,last
    return True,last
Graf1=[[2],[0],[1],[0,2],[3],[3]]
print(good_begin(Graf1))