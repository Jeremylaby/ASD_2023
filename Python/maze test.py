L = ['....', '..#.', '..#.', '....']
print(L[1][2])
from math import inf
from queue import Queue   
def maze(L):
    n=len(L)
    distance=[[0]*n for _ in range(n)]
    distance[0][0]=0
    stack=Queue()
    moves=[(1,0),(-1,0),(0,1)]
    stack.put((0,0,'P',0))
    while not stack.empty():
        x,y,direct,eng=stack.get()
        if x<=n-1 and x>=0 and y>=0 and y<=n-1 and eng>=distance[x][y]:
            if direct=='D':
                z=0
                if x<n-1 and L[x+1][y]!='#':
                    distance[x+1][y]=max(distance[x+1][y],distance[x][y]+1)
                    stack.put((x+1,y,'D',distance[x+1][y]))
                if y<n-1 and L[x][y+1]!='#' :
                    distance[x][y+1]=max(distance[x][y+1],distance[x][y]+1)
                    stack.put((x,y+1,'P',distance[x][y+1]))
            elif direct=='G':
                z=1
                if x>0 and L[x-1][y]!='#':
                    distance[x-1][y]=max(distance[x-1][y],distance[x][y]+1)
                    stack.put((x-1,y,'G',distance[x-1][y]))
                if y<n-1 and L[x][y+1]!='#' :
                    distance[x][y+1]=max(distance[x][y+1],distance[x][y]+1)
                    stack.put((x,y+1,'P',distance[x][y+1]))
            else:
                z=2
                if x>0 and L[x-1][y]!='#' :
                    distance[x-1][y]=max(distance[x-1][y],distance[x][y]+1)
                    stack.put((x-1,y,'G',distance[x-1][y]))
                if y<n-1 and L[x][y+1]!='#' :
                    distance[x][y+1]=max(distance[x][y+1],distance[x][y]+1)
                    stack.put((x,y+1,'P',distance[x][y+1]))
                if x<n-1 and L[x+1][y]!='#' :
                    distance[x+1][y]=max(distance[x+1][y],distance[x][y]+1)
                    stack.put((x+1,y,'D',distance[x+1][y]))
    print(distance)
    return distance[n-1][n-1]
print(maze(L))