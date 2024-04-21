from egz3btesty import runtests


def maze(L):
    n=len(L)
    distance=[[-1]*n for _ in range(n)]
    distance[0][0]=0
    for i in range(n):
        if L[i][0]=='#':break
        distance[i][0]=i
    go_up=[-1 for _ in range(n)]
    go_down=[-1 for _ in range(n)]
    for j in range(1,n):
        for i in range(n):
            if L[i][j]!='#':
                if i>0 and (distance[i][j-1]!=-1 or go_down[i-1]!=-1):
                    go_down[i]=max(distance[i][j-1],go_down[i-1])+1
                elif i==0 and distance[i][j-1]!=-1:
                    go_down[i]=distance[i][j-1]+1
            else:
                go_down[i]=-1
            if L[n-1-i][j]!='#':
                if i>0 and (distance[n-1-i][j-1]!=-1 or go_up[n-i]!=-1):
                    go_up[n-1-i]=max(distance[n-1-i][j-1],go_up[n-i])+1
                elif i==0 and distance[n-1-i][j-1]!=-1:
                    go_up[n-1-i]=distance[n-1-i][j-1]+1
            else:
                go_up[n-1-i]=-1

        for i in range(n):
            distance[i][j]=max(go_down[i],go_up[i])

    return distance[n-1][n-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )
