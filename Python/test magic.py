from math import inf

def magic(C):
    n = len(C)
    dp = [-inf] * n
    dp[0] = 0
    for i in range(n-1):
        if dp[i]!=-inf:
            Gold_in_chest,dors=C[i][0],C[i][1:]
            print(dors)
            for cost,dest in dors:
                if dest>i and dp[i]+Gold_in_chest-cost>=0:
                    print(cost,dest)
                    if Gold_in_chest-cost<=10:
                        dp[dest]=max(dp[dest],dp[i]+Gold_in_chest-cost)
                    else:
                        dp[dest]=max(dp[dest],dp[i]+10)
    print(dp)
    return dp[n-1]
C = [ [8, [ 6, 3], [ 4, 2], [7, -1]], # 0
[100, [12, 2], [21, 3], [0,-1]], # 1
[9, [11, 3], [ 0,-1], [7,-1]], # 2
[15, [ 0,-1], [ 1,-1], [0,-1]] ]
print(magic(C))
C2=[[2, [5, 1], [1, 6], [1, 8]],        #0
    [2, [7, 2], [1, 4], [1, 2]],        #1
    [89, [91, 3], [75, 8], [84, 6]],    #2
    [8, [6, 4], [10, 6], [7, 5]],       #3
    [4, [5, 5], [1, 7], [3, 5]],        #4
    [10, [11, 6], [0, 6], [4, 6]],      #5
    [1, [0, 7], [0, 7], [6, 7]],        #6
    [57, [51, 8], [45, 8], [50, 8]],    #7
    [2, [6, 9], [7, 9], [0, 9]],        #8
    [6, [3, -1], [8, -1], [1, -1]]]     #9
[0, -inf, -inf, -inf, -inf, -inf, 1, 2, 12, 14]
T=[[0]*8 for _ in range(2)]
print(len(T))
print(len(T[0]))
print(T)