def left(k):return 2*k+1
def right(k):return 2*k+2
def parent(k):return (k-1)//2
def max_heapify(Arr,k):
    l=left(k)
    r=right(k)
    if l< len(Arr) and Arr[l]>Arr[k]:
        largest=l
    else:
        largest=k
    if r< len(Arr) and Arr[r]>Arr[k]:
        largest=r
    if largest!=k:
        Arr[largest],Arr[k]=Arr[k],Arr[largest]
        max_heapify(Arr,largest)
def min_heapify(Arr,k):
    l=left(k)
    r=right(k)
    if l< len(Arr) and Arr[l]<Arr[k]:
        largest=l
    else:
        largest=k
    if r< len(Arr) and Arr[r]<Arr[k]:
        largest=r
    if largest!=k:
        Arr[largest],Arr[k]=Arr[k],Arr[largest]
        min_heapify(Arr,largest)
def build_min_heap(Arr):
    p=parent(len(Arr)-1)
    for i in range (p,-1,-1):
        min_heapify(Arr,i)
def build_max_heap(Arr):
    p=parent(len(Arr)-1)
    for i in range (p,-1,-1):
        max_heapify(Arr,i)
class mediana:
    def __init__(self):
        self.mediana=(0,0)
        self.size=0
        self.maxsize=0
        self.minheap=[]
        self.maxheap=[]

Smediana = mediana()
def insert(mediana,val):
    if mediana.mediana == (0,0):
        mediana.mediana = (val,1)
    elif mediana.mediana[1]==1:
        med=mediana.mediana[0]
        if mediana.maxsize==mediana.size:
            max1=max(val,med)
            min1=min(val,med)
            mediana.maxsize+=1
            mediana.size+=1
            mediana.maxheap.append(max1)
            mediana.minheap.append(min1)
            build_min_heap(mediana.maxheap)
            build_max_heap(mediana.minheap)
            max1=mediana.maxheap[0]
            min1=mediana.minheap[0]
            mediana.mediana=((max1+min1)//2,0)
        else:#do dokończenia trzeba bybyło zmienić też build heap żeby wyznaczał parenta dla mediana.size -1
            max1=max(val,med)
            min1=min(val,med)
    else:
        if mediana.maxsize==mediana.size:
            if val>mediana.maxheap[0]:
                val,mediana.maxheap[0]=mediana.maxheap[0],val
                build_min_heap(mediana.maxheap)
                mediana.mediana=(val,1)
            elif val<mediana.minheap[0]:
                val,mediana.minheap[0]=mediana.minheap[0],val
                build_max_heap(mediana.minheap)
                mediana.mediana=(val,1)
            else:
                mediana.mediana=(val,1)
tab=[17,90,46,18,45,87,46]
build_max_heap(tab)
print(tab)
build_min_heap(tab)
print(tab)
insert(Smediana,5)
print(Smediana.maxheap)
print(Smediana.minheap)
insert(Smediana,7)
print(Smediana.maxheap)
print(Smediana.minheap)
insert(Smediana,4)
print(Smediana.maxheap)
print(Smediana.minheap)
insert(Smediana,12)
print(Smediana.maxheap)
print(Smediana.minheap)
insert(Smediana,34)
print(Smediana.maxheap)
print(Smediana.minheap)
insert(Smediana,70)
print(Smediana.maxheap)
print(Smediana.minheap)
insert(Smediana,43)
print(Smediana.maxheap)
print(Smediana.minheap)
print(Smediana.mediana[0])
