from math import inf
from queue import PriorityQueue
# idea jest taka że tworzymy tablice kosztów gdzie będziemy relaxować koszty związane z podróżą 
# oraz z różnymi wariantmi zapasu paliwa dla danego wierzchołka czy opłaca się dojechać np z 2 litrami zapasu\
# z poprzedniej stacji 
# czy przyjechać na tą z pustym bakiem i zatankować na następny odcinek
def relax(G,cost,dist,d_cost,u,v):
    for i in range(dist,len(d_cost[v])):
        for j in range(i-dist,len(d_cost[v])):
            d_cost[v][j]=min(d_cost[v][j],d_cost[u][i]+j*cost)
def cheapest_way_refuel(G,A,B,tank):
    d_cost=[[inf]*(tank+1) for _ in range(len(G))]
    visited=[False for _ in range(len(G))]
    for i in range(len(d_cost[0])):
        d_cost[0][i]=G[0][1]*i
    Q=PriorityQueue()
    Q.put((0,A))
    while not Q.empty():
        c,u=Q.get()
        for v,dist in G[u][0]:
            if not visited[u] and dist<=tank:
                relax(G,G[v][1],dist,d_cost,u,v)
                Q.put((d_cost[v][0],v))
        visited[u]=True
    return d_cost[B][0]




graph = [[[(1, 5), (2, 7)], 8],
         [[(0, 4), (2, 3), (3, 5)], 5],
         [[(0, 7), (1, 3), (3, 4)], 3],
         [[(1, 5), (2, 4), (4, 6)], 2],
         [[(3, 6)], 1]]
tab=[[[(1,0),1,0],0],
     [[(4,5),(4,5)],6]]
print(cheapest_way_refuel(graph,0,4,6))
