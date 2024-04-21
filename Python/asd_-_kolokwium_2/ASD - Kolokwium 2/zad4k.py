from zad4ktesty import runtests

def falisz ( T ):
    n=len(T)

    DP=[[0]*n for _ in range(n)]
    for i in range(1,n):
        DP[i][0]=DP[i-1][0]+T[i][0]
        DP[0][i]=DP[0][i-1]+T[0][i]
    for i in range(1,n):
        for j in range(1,n):
            DP[i][j]=T[i][j]+min(DP[i-1][j],DP[i][j-1])
    

    return DP[i][j]

runtests ( falisz )
