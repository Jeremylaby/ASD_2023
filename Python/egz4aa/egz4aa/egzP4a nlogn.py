from egzP4atesty import runtests 
# to rozwiazanie polega na tym ze tworzymy tablice ciagu 
# tablice S i jezeli patrzymy na ekement z tablicy T który jest wiekszy niz ten na ostatniej pozycji w S to appendujemy go 
#a jezeli nie to szukamy indeksu w tablicy za pomoca binsearcha szukamy najmniejszego elementu wiekszego niz nasze T[i]
# i zmieniamy ten element na tej pozycji
def insert_pos(val,l,r,S):
    while r-l>1:
        k=l+(r-l)//2
        if S[k]>=val:
            r=k
        else:
            l=k
    return r
def mosty ( T ):
    T.sort(key=lambda x:(x[0],x[1]))
    S=[]
    S.append(T[0][1])
    for i in range(1,len(T)):
        if T[i][1]>=S[-1]:
            S.append(T[i][1])
        else:
            S[insert_pos(T[i][1],-1,len(S)-1,S)]=T[i][1]
    
    #tutaj proszę wpisać własną implementację 
    return len(S)

runtests ( mosty, all_tests=True )