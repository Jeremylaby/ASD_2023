from zad6ktesty import runtests 

def haslo ( S ):
    n=len(S)
    DP=[0 for _ in range(n)]
    DP[0]=1
    print(S)
    if int(S[:2])<=26:
        DP[1]=2
    else:
        DP[1]=1
    for i in range(2,n):
        if int(S[i])==0:
            if int(S[i-1])==0 or int(S[i-1])>=3:
                return 0
            DP[i]=DP[i-2]
            
        elif int(S[i-1:i+1])<=26:
            if S[i-1]=='0':
                DP[i]=DP[i-1]
            else:
                DP[i]=DP[i-2]+DP[i-1]
        else:
            DP[i]=DP[i-1]
    return DP[n-1]

runtests ( haslo )