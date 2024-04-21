from kol1testy import runtests
#Stanisław Barycki
#na początku przepisuje tablice T do tablicy T2 jako tablice krotek(wartosc T,pozycja)
#ustawiam zmienna sumuj zeby pamietala kty co do wielkosci element
#przesuwajac przedzial sprawdzam czy dodany nowy element jest taki sam jak ten ktory wychodzi 
#czyli albo obydwa sa wieksze od ktego elementu albo obydwa mniejsze
#oraz sprawdzam czy kty element dalej nalezy do przedziału
#jezeli wszystko false to szukam nowego katego elementu:
#dany przedział z tablicy przepisuje sobie do nowej tablicy tab
#po czym za pomocą QS sortuje tą tablice i czwartą największą liczbe dodaje do sumy 
def partition(A,p,r):
    x=A[r][0]
    i=p-1
    for j in range (p,r):
        if A[j][0]<=x:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1
def QS(A,p,r):
    while p<r:
        q=partition(A,p,r)
        if q-p<r-q:
            QS(A,p,q-1)
            p=q+1
        else:
            QS(A,q+1,r)
            r=q-1

def ksum(T, k, p):
    n=len(T)
    sum=0
    T2=[]
    for i in range (len(T)):
        T2.append((T[i],i))
    i=0
    Tab=T2[i:i+p]
    QS(Tab,0,len(Tab)-1)
    sum+=Tab[len(Tab)-k][0]
    sumuj=Tab[len(Tab)-k]
    for i in range (1,n-p+1):
        if T2[i-1][0]>sumuj[0] and T2[i+p-1][0]>sumuj[0] and T2[sumuj[1]][1]>=i:
            sum+=sumuj[0]
        elif T2[i-1][0]<sumuj[0] and T2[i+p-1][0]<sumuj[0] and T2[sumuj[1]][1]>=i:
            sum+=sumuj[0]
        else:
            Tab=T2[i:i+p]
            QS(Tab,0,len(Tab)-1)
            sum+=Tab[len(Tab)-k][0]
            sumuj=Tab[len(Tab)-k]
           

    # tu prosze wpisac wlasna implementacje
    return sum


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
