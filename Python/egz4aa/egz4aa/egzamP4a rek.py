from egzP4atesty import runtests 
from math import inf
#Rekurencyjna wersja
def f(T,D,i):
    if i==0:
        return 1
    if D[i]!=-1:
        return D[i]
    maks=1
    for j in range(i):
        if T[j]<=T[i]:
            maks=max(maks,f(T,D,j)+1)
    D[i]=maks
    return D[i]

def mosty ( T ):
    T.sort(key=lambda x:(x[0],x[1]))
    T2=[ T[i][1] for i in range (len(T))]
    T2.append(inf)
    D=[ -1 for i in range(len(T2))]
    
    #tutaj proszę wpisać własną implementację 
    return f(T2,D,len(T2)-1) -1

runtests ( mosty, all_tests=True )