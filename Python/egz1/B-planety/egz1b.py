from egz1btesty import runtests
from queue import PriorityQueue
from math import inf
#Stanisław Barycki 
# pomysł na to zadanie jest taki tworze yablice dwuelementową w której będę zapisywał koszty podróży
# i sprawdzał czy bardziej opłaca się dojechać z pustym bakiem czy z nadwyższką paliwa lub za pomocą teleportacji
# na polu DP[i][j] zapisujemy wartość minimum z DP[i-1][distance] distance z poprzedniej planety lub z dojechania tu na pustym baku plus dotankowanie




def planets( D, C, T, E ):
    DP=[[inf]*(E+1) for _ in range(len(D))]
    tank=E+1
    for i in range(E+1):
        DP[0][i]=i*C[0]
    if T[0][0]!=0:
        DP[T[0][0]][0]=T[0][1]
    for i in range(1,len(D)):
        for j in range(0,tank):
            distance =D[i]-D[i-1]
            
            if distance +j < tank:
                DP[i][j]=min(DP[i-1][distance+j],DP[i][j-1]+C[i],DP[i][j])
            else: 
                DP[i][j]=min(DP[i][j-1]+C[i],DP[i][j])
            if T[i][0]!=i and j==0:
                DP[T[i][0]][0]=min(DP[T[i][0]][0],DP[i][0]+T[i][1])
           
    # tu prosze wpisac wlasna implementacje
    return DP[len(D)-1][0]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )
