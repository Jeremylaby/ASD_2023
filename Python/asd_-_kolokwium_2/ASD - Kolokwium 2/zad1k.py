from zad1ktesty import runtests
from math import inf
def f(a,b,DP,S):
    if a==b:
        if S[b]=='0':
            return 1
        else:
            return 0
    if DP[a][b]!=None:
        return DP[a][b]
    if S[b]=='0':
        DP[a][b]=f(a,b-1,DP,S)+1
    else:
        DP[a][b]=f(a,b-1,DP,S)-1
    return DP[a][b]


def roznica( S ):
    n=len(S)
    DP=[[None]*n for _ in range(n)]
    #for i in range(n):
        #f(i,n-1,DP,S)
    maks=-1
    for a in range(n):
        if S[a]=='0':
            DP[a][a]=1
        else:
            DP[a][a]=-1
    for a in range(n):
        for b in range(a+1,n):
            if S[b]=='0':
                DP[a][b]=DP[a][b-1]+1
            else:
                DP[a][b]=DP[a][b-1]-1
            maks=max(maks,DP[a][b])



    #Tutaj proszę wpisać własną implementację
    return maks

runtests ( roznica )