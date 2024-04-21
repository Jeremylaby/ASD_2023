from zad7ktesty import runtests 
from queue import Queue
def irrigation(T,D):
    n=len(T)
    m=len(T[0])
    moves=[(-1,0),(1,0),(0,1),(0,-1)]
    visited=[[False]*m for _ in range(n)]
    N=[0 for _ in range(len(D))]
    k=0
    for tree in D:
        Q=Queue()
        Q.put((0,tree))
        suma=0

        while not Q.empty():
            i,j=Q.get()
            if not visited[i][j]:
                visited[i][j]=True
                suma+=T[i][j]
                for l in range(4):
                    x,y=moves[l]
                    i2,j2=i+x,j+y
                    if i2>=0 and i2<=n-1 and j2>=0 and j2<=m-1 and T[i2][j2]!=0 and not visited[i2][j2]:

                        Q.put((i2,j2))
        N[k]=suma
        k+=1
    return N
def knapsack(item_list,l):
    n=len(item_list)
    DP=[[0]*(l+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,l+1):
            item_size,item_val=item_list[i-1]
            if item_size>j:
                DP[i][j]=DP[i-1][j]
            else:
                DP[i][j]=max(DP[i-1][j],DP[i-1][j-item_size]+item_val)
    return DP[n][l]
def ogrodnik (T, D, Z, l):
    N=irrigation(T,D)
    item_list=[(N[i],Z[i]) for i in range(len(Z))]
    return knapsack(item_list,l)
runtests( ogrodnik, all_tests=True )
