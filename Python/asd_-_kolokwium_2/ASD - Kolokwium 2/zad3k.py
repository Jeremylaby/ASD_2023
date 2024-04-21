from zad3ktesty import runtests
from math import inf
def ksuma( T, k ):
    n=len(T)
    DP=[inf for _ in range(n)]
    minimum=inf
    for i in range(k):
        DP[i]=T[i]
        minimum=min(minimum,T[i])
    if n==k:
        return minimum
    minimum=inf
    for i in range(k,n):
        minn=inf
        for j in range(i-k,i):
            minn=min(minn,DP[j])
        DP[i]=T[i]+minn
        if i>=n-k:  
            minimum=min(minimum,DP[i])

    return minimum
    
runtests ( ksuma )