tab=[0,1,2,3,4,5]
print(tab[0:4])
tab2=[(1,1),(2,2),(3,3),(4,4)]
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
        if q-p>r-q:
            QS(A,p,q-1)
            p=q+1
        else:
            QS(A,q+1,r)
            r=q-1
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