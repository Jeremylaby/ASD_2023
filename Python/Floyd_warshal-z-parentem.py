from math import inf

def floyd_warschal(G):
    n= len(G)
    d=[[inf]*n for _ in range(n)]
    parent=[[None]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i==j:d[i][j]=0
            elif G[i][j]!=0:
                d[i][j]=G[i][j]
                parent[i][j]=i
    for i in range(n):
        for u in range(n):
            for v in range(n):
                if d[u][v]>d[u][i]+d[i][v]:
                    d[u][v]=d[u][i]+d[i][v]
                    parent[u][v]=parent[i][v]
    return d,parent
def print_start_end(parent,d,start,end):
    if d[start][end]==inf:
        print("None")
        return
    while end is not None:
        print(end,"<(",d[start][end],")-",end=" ")
        end=parent[start][end] 
    print("")
Graf=[[0,5,15,0,0,0,0],
      [0,0,3,16,5,0,0],
      [0,0,0,10,0,18,0],
      [0,0,0,0,0,0,0],
      [0,0,0,0,0,0,3],
      [0,0,0,1,0,0,2],
      [0,0,2,3,0,0,0]]
Graf2=[[0,5,15,0,0,0,0],
      [5,0,3,16,5,0,0],
      [15,3,0,10,0,18,2],
      [0,16,10,0,0,1,3],
      [0,5,0,0,0,0,3],
      [0,0,18,1,0,0,2],
      [0,0,2,3,3,2,0]]
d,parent=floyd_warschal(Graf)
print_start_end(parent,d,0,6)
print_start_end(parent,d,3,6)
print_start_end(parent,d,0,5)
print("")
d,parent=floyd_warschal(Graf2)
print_start_end(parent,d,0,6)
print_start_end(parent,d,3,6)
print_start_end(parent,d,0,5)
