from zad8testy import runtests
from queue import Queue
from queue import PriorityQueue
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
                if i2>=0 and i2<=n-1 and j2>=0 and j2<=m-1 and not visited[i2][j2] and T[i2][j2]!=0:
                    Q.put((i2,j2))
    return suma
def plan(T):
    n=len(T)
    m=len(T[0])
    Stop=1

    visited=[[False]*m for _ in range(n)]
    Tank=[0 for _ in range(m)]
    for j in range(m):
        if not visited[0][j] and T[0][j]!=0:
            Tank[j]=fuel_in_area(n,m,visited,j,T)
    P_Q=PriorityQueue()
    fuel=Tank[0]
    for j in range(1,m):
        fuel-=1
        if fuel==-1:
            Stop+=1
            fuel+=P_Q.get()*(-1)
        if Tank[j]!=0:
            P_Q.put((Tank[j])*(-1))
    return Stop



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )

