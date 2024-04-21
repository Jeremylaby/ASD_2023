def DFS(v,G,A,vis):
    for i in range (len(G)):
        if vis[v][i]==1:
            vis[v][i],vis[i][v]=0,0
            DFS(i,G,A,vis)
    A.append(v)


def Euler_cycle(G,v):
    vis=G
    A=[]
    DFS(v,G,A,vis)
    for i in range(len(G)):
        for j in range(len(G)):
            if vis[i][j]==1: return A,False
    return A,True

Graf=[[0,0,0,0,1,0],
      [1,0,0,0,0,1],
      [0,1,0,1,0,0],
      [0,1,0,0,0,0],
      [0,0,1,0,0,0],
      [0,0,1,0,0,0]]
Graf2=[[0,1,0,0,1,0],
       [1,0,1,1,0,1],
       [0,1,0,1,1,1],
       [0,1,1,0,0,0],
       [1,0,1,0,0,0],
       [0,1,1,0,0,0]]

A,flag=Euler_cycle(Graf,0)
for i in range(len(A)-1,-1,-1):
    print(A[i])
print("\n")
A,flag=Euler_cycle(Graf2,0)
for i in range(len(A)-1,-1,-1):
    print(A[i])