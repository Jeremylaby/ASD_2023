from queue import Queue
T=[[0]*3 for _ in range(6)]
print(T)
print(len(T))
print(len(T[0]))
moves=[[-1,0],[1,0],[0,-1],[0,1]]
i,j=3,3
for k in range(4):
    x,y=moves[k]
    i2,j2=i+x,j+y
    print(i2,j2)
T=[[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
 [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
 [0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1], 
 [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
 [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
 [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
def fuel_in_area(n,m,visited,j,T):
    i=0
    suma=0
    Q=Queue()
    moves=[[-1,0],[1,0],[0,-1],[0,1]]
    Q.put((i,j))
    while not Q.empty():
        i,j=Q.get()
        if not visited[i][j]:
            visited[i][j]=True
            suma+=T[i][j]
            for k in range(4):
                x,y=moves[k]
                i2,j2=i+x,j+y
                if i2>=0 and i2<=n and j2>=0 and j2<=m-1 and not visited[i2][j2] and T[i2][j2]!=0:
                    Q.put((i2,j2))
    return suma
def plan(T):
    n=len(T)
    m=len(T[0])
    visited=[[False]*m for _ in range(n)]
    Tank=[0 for _ in range(m)]
    for j in range(m):
        if not visited[0][j] and T[0][j]!=0:
            Tank[j]=fuel_in_area(n,m,visited,j,T)
    return Tank
print(plan(T))