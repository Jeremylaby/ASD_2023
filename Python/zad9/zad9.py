from zad9testy import runtests
from math import inf
from queue import PriorityQueue
def min_cost( O, C, T, L ):
    n=len(O)
    A=[(O[i],C[i]) for i in range(n)]
    n+=2
    A.append((0,0))
    A.append((L,0))
    cost_a=[inf for _ in range(n)]
    cost_b=[inf for _ in range(n)]
    A.sort()
    Q_a=PriorityQueue()
    Q_b=PriorityQueue()
    Q_T2=PriorityQueue()
    cost_a[0]=0
    cost_b[n-1]=0
    last_min_rest=(0,0)
    for i in range(1,n):
        while A[i][0]>last_min_rest[1]+T and not Q_a.empty():
            last_min_rest=Q_a.get()
        cost_a[i]=last_min_rest[0]+A[i][1]
        Q_a.put((cost_a[i],A[i][0])) 
    last_min_rest=(0,L)
    for i in range(n-2,-1,-1):
        while A[i][0]<last_min_rest[1]-T and not Q_b.empty():
            last_min_rest=Q_b.get()
        cost_b[i]=last_min_rest[0]+A[i][1]
        Q_b.put((cost_b[i],A[i][0]))
    last_min_rest=(0,0)
    min_cost=inf
    for i in range(1,n):
        while A[i][0]>last_min_rest[1]+T*2 and not Q_T2.empty():
            last_min_rest=Q_T2.get()
        min_cost=min(min_cost,last_min_rest[0]+cost_b[i])
        Q_T2.put((cost_a[i],A[i][0]))
            # tu prosze wpisac wlasna implementacje
    return min_cost

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = True )
