from zad3testy import runtests
#Stanislaw Barycki
#moj algorytm działa nastepujaco najpierw slowa ktore mogly by byc odbicie lustrzanym odwraca 
# tu sprawdzane jest ktory napis bylby wyzej leksykografcznie ten odwrocony czy nie
# używa QS do posortowania tablicy leksykograficznie
# zlicza max i go zwraca

def partition(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]  
    return i+1
def QS(A,p,r):
    while p<r:
        q=partition(A,p,r)
        QS(A,p,q-1)
        p=q+1
    return 
def strong_string(T):
    max2=0
    for i in range (0,len(T)):
        slowo = T[i]
        if slowo[::-1]<slowo:
            T[i]=slowo[::-1]
    QS(T,0,len(T)-1)
    max1=1
    curr=1
    for i in range (0,len(T)-1):
        if(T[i]==T[i+1]):
            curr+=1
            max1=max(max1,curr)
        else: curr=1


    # tu prosze wpisac wlasna implementacje
    return max1


# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests( strong_string, all_tests=True )
