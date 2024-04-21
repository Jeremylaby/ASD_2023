from egzP6atesty import runtests 
def more_letters(s1,s2):#== less_nums
    n=len(s1)
    count_s1=0
    count_s2=0
    for i in range(n):
        if s1[i]>='0' and s1[i]<='9':
            count_s1+=1
        if s2[i]>='0' and s2[i] <='9':
            count_s2+=1
    return count_s1-count_s2



def partition(left,right,A):
    x=A[right]
    i=left-1
    for j in range(left,right):
        if len(A[j])>len(x):
            i+=1
            A[j],A[i]=A[i],A[j]
        elif len(A[j])==len(x) and more_letters(A[j],x)<=0:
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
def google ( H, s ):
    str=Quick_Select(0,len(H)-1,H,s)
    #tutaj proszę wpisać własną implementację
    return str[s-1]


runtests ( google, all_tests=True )