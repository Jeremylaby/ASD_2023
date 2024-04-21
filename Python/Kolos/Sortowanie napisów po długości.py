def partition(A,p,r):
    x=len(A[r])
    i=p-1
    for j in range(p,r):
        if len(A[j])<=x:
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
    return
def napis(T):
    QS(T,0,len(T)-1)
    for i in range(len(T)):
        print(T[i])
    return
def insertion_sort(bucket):
    for i in range (1, len (bucket)):
        var = len(bucket[i])
        rem=i
        j = i - 1
        while (j >= 0 and var < len(bucket[j])):
            bucket[j + 1] = bucket[j]
            j = j - 1
        bucket[j + 1] =bucket[i]
def bucket_sort(input_list):
    # Find maximum value in the list and use length of the list to determine which value in the list goes into which bucket 
    max1 = len(input_list[0])
    for i in range (1,len(input_list)):
        max1=max(max1,len(input_list[i]))
    size=max1/len(input_list)

    # Create n empty buckets where n is equal to the length of the input list
    buckets_list= []
    for x in range(len(input_list)):
        buckets_list.append([]) 

    # Put list elements into different buckets based on the size
    for i in range(len(input_list)):
        j = int (len(input_list[i]) / size)
        if j != len (input_list):
            buckets_list[j].append(input_list[i])
        else:
            buckets_list[len(input_list) - 1].append(input_list[i])

    # Sort elements within the buckets using Insertion Sort
    for z in range(len(input_list)):
        insertion_sort(buckets_list[z])
            
    # Concatenate buckets with sorted elements into a single list
    final_output = []
    for x in range(len (input_list)):
        final_output = final_output + buckets_list[x]
    return final_output

T=["pies","kot","kot","parowka","rak","ptak","jablko","ananas"]
x=[]
Y=[("tak",2)]
x.append(T[0])
print(x[0])
print(Y[0][0])
if T[1]==T[2]:
    print(T[2],"hej")
#napis(T)
print(bucketSort(T))
    max1 =len(T[0])
    min1 =len(T[0])
    n=len(T)-1
    for i in range (1,len(T)):
        max1=max(max1,len(T[i]))
        min1=min(min1,len(T[i]))
    p=0
    while n>=0 and len(T[n])==max1:
        n-=1
    while p<n and len(T[p])==min1:
        p+=1