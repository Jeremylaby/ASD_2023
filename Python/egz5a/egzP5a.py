from egzP5atesty import runtests 
#pomysł za gorszą złożoność jest taki że z wykorzystaniem tablicy spamiętującej DP[a][b]rozważamy przedziały a b 
# zwracamy minimum z liczby b i przedziału kończącego się na b 
# f(a,b)= if a==b T[a] min (T[b],f(a,b-1))
def f(a,b,DP,T):
    if a==b:
        return T[b]
    if DP[a][b]!=-1:
        return DP[a][b]
    DP[a][b]=min(T[b],f(a,b-1,DP,T))
    return DP[a][b]
def inwestor ( T ):
    n=len(T)
    maks=0
    DP=[[-1]*n for _ in range(n)]
    for i in range(n):
        for j in range(i,n):
            maks=max(maks,(j-i+1)*f(i,j,DP,T))

    return maks

runtests ( inwestor, all_tests=True)