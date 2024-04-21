class vertex():
    def __init__(self):
        self.visited=0
        self.layer=0
        self.parent=None
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
def longer( G, s, t ):
    BFS(G,s)
    if t.visited=False: return None
    len=t.layer
    curr=t
    parent=t.parent
    while curr!=s:
        flag=0
        higher=0
        for u in G[curr]:
            if u.layer<curr.layer and u!=parent:
                flag=1
                break
            else if u!=son
    # tu prosze wpisac wlasna implementacje
    return (0,0)
