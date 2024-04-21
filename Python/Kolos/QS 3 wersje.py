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
def QS2(A,p,r):
    while p<r:
        q=partition(a,P,R)
        if q-p>r-q:
            QS2(A,p,q-1)
            p=q+1
        else:
            QS2(A,q+1,r)
            r=q-1
    return
def QS_rek(A,p,r):
    if p<r:
        q=partition(A,p,r)
        QS_rek(A,p,q-1)
        QS_rek(A,q+1,r)