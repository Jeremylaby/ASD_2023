def left(i):
    return i*2+1
def right(i):
    return i*2+2
def parent(i):
    return (i-1)//2
def heapify(T,i,n):
    max_val_index=i
    l=left(i)
    r=right(i)
    if l<n and T[l]>T[max_val_index]:max_val_index=l
    if r<n and T[r]>T[max_val_index]:max_val_index=r
    if max_val_index!=i:
        T[max_val_index],T[i]=T[i],T[max_val_index]
        heapify(T,max_val_index,n)
def build_heap(T):
    n=len(T)
    for i in range(parent(n-1),-1,-1):
        heapify(T,i,n)
def heap_sort(T):
    n=len(T)
    for i in range(n-1,-1,-1):
        T[i],T[0]=T[0],T[i]
        heapify(T,0,i)
heap=[10,22,34,14,5,7,32,12,78,2,1,34,67,7,89,32,56,23,53,63,63,23,63,1,12]
build_heap(heap)
n=len(heap)
flag=True
for i in range(n):
    
    if i==0:
        print('#0 root ',heap[i])
    elif flag:
        print('#',i,' l ',heap[i])
        flag=False
    else:
        print('#',i,' r ',heap[i])
        flag=True
heap_sort(heap)
print(heap)