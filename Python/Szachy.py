from collections import deque
import random
def Szachy(T,n):
    vis=[[0] *n for _ in range (n)]
    parent=[[None] *n for _ in range (n)]
    posible_moves=[(-1,1),(0,1),(-1,0),(-1,-1),(1,-1),(1,1),(1,0),(0,-1)]
    Q=deque()
    Q.append((0,0))
    vis[0][0]=1
    while(len(Q)>0):
        i,j=Q[0]
        if i==n-1 and j==n-1 : return vis,parent
        if T[i][j]==0:
            for m,k in posible_moves:
                if i+m>=0 and i+m<n and j+k<n and j+k>=0:
                    if vis[i+m][j+k]==0:
                        Q.append((i+m,j+k))
                        vis[i+m][j+k]=1
                        parent[i+m][j+k]=(i,j)
                        if i+m==n-1 and j+k==n-1 : return vis,parent
        else:
            T[i][j]-=1
            Q.append((i,j))
        Q.popleft()
    return vis,parent
        


Szachownica=[[0,5,1,5,5,5,5,5],
             [5,1,5,1,5,1,1,5],
             [5,5,5,1,1,1,5,1],
             [5,5,5,5,5,5,5,1],
             [5,5,5,5,5,5,5,1],
             [5,5,5,5,5,5,5,1],
             [5,5,5,5,5,5,5,1],
             [5,5,5,5,5,5,5,1]]
Szachownica2=[[0,2,3,4,5,1,2,3],
              [1,2,3,4,5,1,2,3],
              [1,2,3,4,5,1,2,3],
              [1,2,3,4,5,1,2,3],
              [1,2,3,4,5,1,2,3],
              [1,2,3,4,5,1,2,3],
              [1,2,3,4,5,1,2,3],
              [1,2,3,4,5,1,2,3]]
Szachownica3=[[0]*9 for _ in range(9)]
for i in range(9):
    for j in range(9):
        Szachownica3[i][j]=random.randint(1,5)
Szachownica3[0][0]=0
posible_moves=[(-1,1),(0,1),(-1,0),(-1,-1),(1,-1),(1,1),(1,0),(0,-1)]
print("Szachownica1")
vis,parent=Szachy(Szachownica,len(Szachownica))
i,j=len(Szachownica)-1,len(Szachownica)-1
for i in range(len(Szachownica)):
    print(parent[i])
print((i,j))
while i!=0 or j!=0: 
    print(parent[i][j]) 
    i,j=parent[i][j]
print("Szachownica2")
vis,parent=Szachy(Szachownica2,len(Szachownica2))
i,j=len(Szachownica2)-1,len(Szachownica2)-1
for i in range(len(Szachownica2)):
    print(parent[i])
print((i,j))
while i!=0 or j!=0: 
    print(parent[i][j]) 
    i,j=parent[i][j]
print("Szachownica3")
for i in range(9):
    print(Szachownica3[i])
vis,parent=Szachy(Szachownica3,len(Szachownica3))
i,j=len(Szachownica3)-1,len(Szachownica3)-1
for i in range(len(Szachownica3)):
    print(parent[i])
print((i,j))
while i!=0 or j!=0: 
    print(parent[i][j]) 
    i,j=parent[i][j]