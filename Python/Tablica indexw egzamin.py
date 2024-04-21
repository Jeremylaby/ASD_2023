def create_IND(k,m,n):
    START=[0 for _ in range(m)]
    END =[0 for _ in range(m)]
    curr_END=-1
    curr_len=k+m-1    
    for l in range(m):
        START[l]=curr_END+1
        curr_END+=curr_len
        END[l]=curr_END
        curr_len-=1   
    IND=[0 for _ in range(n)] 
    items=0
    kolumna=0
    rzad=0
    while items<n:
        if START[rzad]+kolumna<=END[rzad]:
            IND[START[rzad]+kolumna]=items
            items+=1
        rzad+=1
        if rzad >=m:
            kolumna+=1
            rzad=0
    print(IND)
    return IND,END
def partition(left,right,A,IND):
    x=A[IND[right]][1]
    i=left-1
    for j in range(left,right):
        if A[IND[j]][1]>=x:
            i+=1
            A[IND[j]],A[IND[i]]=A[IND[i]],A[IND[j]]
    A[IND[right]],A[IND[i+1]]=A[IND[i+1]],A[IND[right]]
    return i+1
def Quick_Select(left,right,A,k,IND):
    
    if left<right:
        pivot=partition(left,right,A,IND)
        if pivot<k:
            Quick_Select(pivot+1,right,A,k,IND) 
        elif pivot>k:
            Quick_Select(left,pivot-1,A,k,IND)
    return
A=[(1,3),(2,4),(4,6),(5,8),(5,20),(5,7),(6,8),(7,45),(5,78),(4,78),(34,1),(9,54)]
def zdjecie(T, m, k):
    IND,END=create_IND(k,m,len(T))
    end=END[m-1]
    for i in range(m-2,-1,-1):
        Quick_Select(0,end,T,END[i],IND)
        end=END[i]-1
    return None
zdjecie(A,3,3)
print(A)