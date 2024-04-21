from egz2atesty import runtests
from queue import PriorityQueue
def coal( A, T ):
    n=len(A)
    A=sorted(A)
    A=A[::-1]
    Q=PriorityQueue()
    num=0
    for i in range(n):
        if not Q.empty():
            val=abs(Q.get())
            if val > A[i]:
                Q.put(-(val-A[i]))
            elif val<A[i]:
                num+=1
                Q.put(-(T-A[i]))
        else:
            num+=1
            if A[i]!=T:
                num+=1
                Q.put(-(T-A[i]))





    # tu prosze wpisac wlasna implementacje
    return num

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = False )
