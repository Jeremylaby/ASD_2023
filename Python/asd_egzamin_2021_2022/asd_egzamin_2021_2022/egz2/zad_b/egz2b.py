from egz2btesty import runtests
from math import inf

def magic(C):
    n = len(C)
    dp = [-inf] * n
    dp[0] = 0
    for i in range(n-1):
        if dp[i]!=-inf:
            Gold_in_chest,dors=C[i][0],C[i][1:]
            for cost,dest in dors:
                if dest!=-1 and  dp[i]+Gold_in_chest-cost>=0 and Gold_in_chest-cost<=10:
                        dp[dest]=max(dp[dest],dp[i]+Gold_in_chest-cost)
    if n<=30:
        print(C)
        print(dp)
    if dp[n-1]==-inf:
        return -1
    return dp[n-1]

    

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = True )
