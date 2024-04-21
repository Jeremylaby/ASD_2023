def partition(left,right,A):
    x=A[right]
    i=left-1
    for j in range(left,right):
        if A[j]>=x: #quick select rosnący  czyli znajduje k-tą największą liczbe
            i+=1
            A[j],A[i]=A[i],A[j]
    A[right],A[i+1]=A[i+1],A[right]
    return i+1
def Quick_Select(left,right,A,k):
    
    while left<=right:
        pivot=partition(left,right,A)
        if pivot==k-1:
            return A
        elif pivot>k-1:
            right=pivot-1
        else:
            left=pivot+1
    return A
Tab=[1,54,6,12,8,45,12,3,5,18,45,12,0,67,5,4,674,1,2]
print(Quick_Select(0,len(Tab)-1,Tab,5))