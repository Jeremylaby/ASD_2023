from zad5ktesty import runtests


def garek(A):
    n = len(A)
    
    # Inicjalizacja tablicy dp
    DP = [[(0,0)] * n for _ in range(n)]
    def f(DP,a,b,A):
        if a==b:
            DP[a][b]=(A[a],0)
            return (A[a],0)
        if a+1==b:
            DP[a][b]=(max(A[a],A[b]),min(A[a],A[b]))
            return(max(A[a],A[b]),min(A[a],A[b]))
        if DP[a][b]!=(0,0):
            return DP[a][b]
        if A[a]+f(DP,a+1,b,A)[1]>A[b]+f(DP,a,b-1,A)[1]:
            DP[a][b]=(A[a]+f(DP,a+1,b,A)[1],f(DP,a+1,b,A)[0])
            return (A[a]+f(DP,a+1,b,A)[1],f(DP,a+1,b,A)[0])
        else:
            DP[a][b]=(A[b]+f(DP,a,b-1,A)[1],f(DP,a,b-1,A)[0])
            return (A[b]+f(DP,a,b-1,A)[1],f(DP,a,b-1,A)[0])

    return max(f(DP,0,n-1,A))
    # Ostateczna odpowiedź znajduje się w dp[0][n-1]
runtests ( garek )