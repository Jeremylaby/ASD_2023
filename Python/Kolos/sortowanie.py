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
        if q-p<r-q:
            QS(A,q+1,r)
            r=q-1
        else:
            QS(A,q+1,r)
            r=q-1
Tab=[1, 7, 3, 4, 1]
def sortuj(S):
    QS(S,0,len(S)-1)
    for i in range(len(S)):
        print(S[i])
    n=len(S)
    sum_of_snow=0
    i=0
    for j in range (n-1,-1,-1):
        if S[j]<i:
            break
        sum_of_snow+=S[j]
        sum_of_snow-=i
        i+=1
    print(sum_of_snow)
sortuj(Tab)