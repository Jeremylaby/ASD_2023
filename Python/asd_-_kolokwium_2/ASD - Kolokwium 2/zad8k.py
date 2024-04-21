from zad8ktesty import runtests 

def napraw ( s, t ):
    n=len(s)
    m=len(t)
    DP=[[0]*n for _ in range(m)]
    flag=True
    DP[0][0]=1
    if s[0]==t[0]:
        DP[0][0]=0
    for i in range(1,n):
        if s[i]==t[0] and flag:
            DP[0][i]=DP[0][i-1]
            flag=False
        else:
            DP[0][i]=DP[0][i-1]+1
    flag=True
    for i in range(1,m):
        if t[i]==s[0] and flag:
            DP[i][0]=DP[i-1][0]
            flag=False
        else:
            DP[i][0]=DP[i-1][0]+1
    for j in range(1,n):
        for i in range(1,m):
            if s[j]==t[i]:
                DP[i][j]=DP[i-1][j-1]
            else:
                DP[i][j]=min(DP[i-1][j],DP[i][j-1],DP[i-1][j-1])+1
        

    return DP[m-1][n-1]

runtests ( napraw )