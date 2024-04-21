from zad2testy import runtests
#Stanisław barcki algorytm działa następująca:
#jeśłi zastanowimy sie nad zadaniem to nie jest istotne w jakiej kolejnosci zbieramy śnieg tylko z ilu obszarów łaczniem możemy zebrać ten śnieg 
#bo śnieg topi się równomiernie na cąłym obszarze i nie maróznicy czy zbierzmy np najpierw ([1,3,7,4,5,1]) 7 potem (5-1) potem (4-2) czy 5 -> (7-1)->(4-2)
#ważne jest tylko to że z tych 3 obszarów (czyli tam gdzie wyjściowo jest 7 5 4 bo w pozostałych się w tym czasie stopi ) możemy musimy zebrać śnieg 
#wiec do rozwiazania tego problemu skorzystalem z zmodyfikowanego quick sorta który sortuje do momentu az element wystepujacy na prawo od pivota
#jest mniejszy lub równy miejscu na którym występuje to QS się kończy i nie sortuje reszty tablicy bo po co 
def partition(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<x:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]  
    return i+1
def QS(A,p,r):
    q=r
    if q+1<len(A) and A[q+1]<=len(A)-q:
        return
    while p<r:
        q=partition(A,p,r)

        if q-p>r-q:
            QS(A,p,q-1)
            p=q+1
        else:
            QS(A,q+1,r)
            r=q-1
    return
def snow( S ):
    n=len(S)
    QS(S,0,n-1)
    Sum_of_snow=0
    i=0
    for j in range (n-1,-1,-1):
        if S[j]<=i:
            return Sum_of_snow
        Sum_of_snow+=S[j]
        Sum_of_snow-=i
        i+=1
    # tu prosze wpisac wlasna implementacje
    return Sum_of_snow

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
