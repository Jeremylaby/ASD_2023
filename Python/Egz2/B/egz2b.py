from egz2btesty import runtests
from math import inf
# Stanisław Barycki
#  Algorytm działa następująco tworze tablice DP nxm wypełnioną inf
# następnie iterują  po pierwszej kolumnie zakładając ze dla 0 budynku wybieram i ty parking
#  Następnie iteruje po całej tablicy do każdej komurki wpisuje albo poprzedni wybór parkingu czyli DP[i-1][j]
#  albo wybieram ten parking (czyli i-ty) + to co juz wybrałem DP[i-1][j-1]+abs(Y[i]-X[j])
# W skrócie albo wybieram i-ty parking dla j-tego budynku albo nie wybieram i zostawiam poprzednie przypisanie
# f(i,j) i-parking j-budynek
# f(i,j)=min(f(i-1,j-1)+abs(X[j]-Y[i]),f(i-1,j))
# zlożoność czasowa i pamięciowa O(nm)
def parking(X,Y):
  m=len(X)
  n=len(Y)
  DP=[[inf]*m for _ in range(n)]
  DP[0][0]=abs(X[0]-Y[0])
  for i in range(1,n):
    DP[i][0]=min(DP[i-1][0],abs(X[0]-Y[i]))
  for i in range(1,n):
    for j in range(1,m):
      DP[i][j]=min(DP[i-1][j-1]+abs(X[j]-Y[i]),DP[i-1][j])
  # tu prosze wpisac wlasna implementacje
  return DP[n-1][m-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True )
