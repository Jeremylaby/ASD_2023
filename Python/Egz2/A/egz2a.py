from egz2atesty import runtests
#Stanisław Barycki
# dla Każdego punktu sprawdza wśród pozostałych nad iloma dominuje
#złożnosość czasowa O(n^2)

def dominance(P):
  n=len(P)
  MAKS=0
  for i in range(n):
    suma=0
    for j in range(n):
      x1,y1=P[i]
      x2,y2=P[j]
      if i!=j and x1>x2 and y1>y2:
        suma+=1
    MAKS=max(MAKS,suma)
  return MAKS
    


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )
