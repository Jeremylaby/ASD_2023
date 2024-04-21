from egzP4atesty import runtests 
#ogólnie ten algorytm jest defakto problemem najdłuższego podciągu po 2 współrzędnych mostu
# dla lepszej złożoności stawiam że trzeba wykorzystać binsearcha
def mosty ( T ):
    podciag=[ 1 for _ in range(len(T))]
    maks=0
    T.sort(key=lambda x:(x[0],x[1]))
    for i in range(len(T)):
        for j in range(i):
            if T[j][1]<=T[i][1] and podciag[i]<=podciag[j]+1:
                podciag[i]=podciag[j]+1
                maks=max(maks,podciag[i])
    #tutaj proszę wpisać własną implementację 
    return maks

runtests ( mosty, all_tests=True )