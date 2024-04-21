A=[1,2,3,4,5]
B=[[0,'']]*10
B[0][1]="tata"
print(A[:1])
print(B[0],[1])
def kod_slowa(S):
    kod=0
    for i in range (len(S)):
        kod+=ord(S[i])
    return kod
def strong_string(T):
    max1=0
    for i in T:
        max1=max(max1,kod_slowa(i))
    max2=0
    C=[[0,'']]*(max1+10)
    for i in T:
        kod=kod_slowa(i)
        if C[kod][1]==i or C[kod][1]=='' or C[kod][1] == i[::-1]:
            C[kod][1]=i
            C[kod][0]+=1
            max2=max(max2,C[kod][0])
        else:
            while C[kod][1]!=i or C[kod][1]!='' or C[kod][1] != i[::-1]:
                kod+=1
            C[kod][1]=i
            C[kod][0]+=1
            max2=max(max2,C[kod][0])
            

def merge_sort(A):
    if len(A)>1:
        dziel=len(A)//2
        left=A[:dziel]
        right=A[dziel:]
        merge_sort(left)
        merge_sort(right)
        i=0
        j=0
        k=0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1


        
def strong_string(T):
    max2=0
    for i in range (0,len(T)):
        slowo = T[i]
        if slowo[::-1]<slowo:
            T[i]=slowo[::-1]
    merge_sort(T)
    max1=1
    curr=1
    for i in range (0,len(T)-1):
        if(T[i]==T[i+1]):
            curr+=1
            max1=max(max1,curr)
        else: curr=1
b=[[0,0]]*20
b[10]= [1,'pies']
b[10][0]+=10
## 2 próba
def kod_slowa(S):
    kod=0
    for i in range (len(S)):
        kod+=ord(S[i])
        kod-=96
    return kod
def strong_string(T):
    max1=0
    n=len(T)
    for i in range (0,len(T)):
        slowo = T[i]
        max1=max(max1,kod_slowa(slowo))
    max2=0
    max1=max(max1,n)
    C=[[0,0]]*(max1+1)
    n=len(C)
    for i in T:
        kod=kod_slowa(i)
        if C[kod][0]==0:
            C[kod]=[1,i]
        elif C[kod][1]==i or C[kod][1]==i[::-1]:
            C[kod][0]+=1
            max2=max(max2,C[kod][0])
        else:
            while  C[kod][1]!=i and C[kod][1]!=i[::-1]:
                kod+=1
                if kod==n:
                    kod=0
                if C[kod][0]==0:
                    C[kod]=[0,i]
                    break
            C[kod][0]+=1
            max2=max(max2,C[kod][0])
def merge_sort2(A):
    n=len(A)
    i=1
    while i<n and A[i]>=A[i-1]:
        i+=1
    kl=i
    while True:
        print(kl)
        pp=kl
        if kl == n:
            return          
        left=A[:kl]
        kp=pp+1
        while kp<n and A[kp]>=A[kp-1]:
            kp+=1
        right=A[pp:kp]
        i=j=k=0
        print(left,right)
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1
        print(A)
        kl=kp

T=[0,2,6,5,7,8,10,6,5,4]
print(T[:5])
print(T[5:10])
merge_sort2(T)
print(T)