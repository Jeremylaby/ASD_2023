tmp=1
    for i in range(n):
        flag =True
        if i%2==0:
            if tmp >=1:
                for j in range(tmp,n):
                    if flag and L[j][i]=="#":
                        flag=False
                        tmp=j-2
                        if i<n-1 and L[j-1][i+1]!="#":
                            Str_maze[j-1][i+1]=Str_maze[j-1][i]+1
                    elif Str_maze[j-1][i]>=0:
                        Str_maze[j][i]=Str_maze[j-1][i]+1
                    elif i>0 and Str_maze[j][i-1]>0:
                        Str_maze[i][j]=Str_maze[j][i-1]+1
                    elif flag==False:
                        if L[i][j]!="#":
                            if Str_maze[j-1][i]>=0:
                                Str_maze[j][i]=Str_maze[j-1][i]+1
                            elif i>0 and Str_maze[j][i-1]>=0:
                                Str_maze[j][i]=Str_maze[j][i-1]+1
                        if i<n-1 and L[j][i+1]!="#":
                            if Str_maze[j-1][i+1]>=0:
                                Str_maze[j][i+1]=Str_maze[j-1][i+1]
                            elif i>0 and Str_maze[j][i]>=0:
                                Str_maze[j][i+1]=Str_maze[j][i]+1
            if flag==False: tmp=n-2
        else:
            if tmp<=n-2:
                for j in range(tmp,-1,-1):
                    if flag and L[j][i]=="#":
                        flag=False
                        tmp=j+2
                        if i<n-1 and L[j+1][i+1]!="#":
                            Str_maze[j+1][i+1]=Str_maze[j+1][i]+1
                    elif Str_maze[j+1][i]>=0:
                        Str_maze[j][i]=Str_maze[j+1][i]+1
                    elif i>0 and Str_maze[j][i-1]>0:
                        Str_maze[i][j]=Str_maze[j][i-1]+1
                    elif flag==False:
                        if L[i][j]!="#":
                            if Str_maze[j+1][i]>=0:
                                Str_maze[j][i]=Str_maze[j+1][i]+1
                            elif i>0 and Str_maze[j][i-1]>=0:
                                Str_maze[j][i]=Str_maze[j][i-1]+1
                        if i<n-1 and L[j][i+1]!="#":
                            if Str_maze[j+1][i+1]>=0:
                                Str_maze[j][i+1]=Str_maze[j+1][i+1]
                            elif i>0 and Str_maze[j][i]>=0:
                                Str_maze[j][i+1]=Str_maze[j][i]+1
                if flag==False: tmp=1

from zad7testy import runtests
#Stanisław Barycki
# Algorytm działa Patrzymy na kolejne kolumny listy L i sprawdzamy czy dłuższa droga prowadzi "od góry"
# długość tej drogi jest zapisywana w tablicy Walk_down a mianowicie większa  wartość  z wartości 
# zapisanej w poprzeniej komórce Wolk_down lub wartości zapisanej w kolumnie "obok" w tablicy Str_maze
#  czy od dołu długości tej drogi są zapisane w tablicy Walk_up analogia do Walk_down
# przeglądamy te dwie listy i maksimumna na danej pozycji zapisujemy w tablicy Str_maze i takim sposobem wypełniamy 
# kolejne kolumny tablicy Str_maze.
#FD(A,B)=max(FD(A-1,B),FS(A,B-1))+1
#FU(A,B)=max(FD(A+1,B),FS(A,B-1))+1
#FS(A,B)=max(FD(A,B),FU(A,B))
def maze( L ):
    n=len(L)
    Str_maze=[[-1]*n for _ in range(n)]
    Str_maze[0][0]=0
    for k in range(n):
        if L[k][0]=="#":break
        Str_maze[k][0]=k
    for i in range(1,n):
        if i%2==0:
            for j in range(n):
                if L[j][i]!="#":
                    if j>0 and (Str_maze[j][i-1]!=-1 or Str_maze[j-1][i]!=-1):
                        Str_maze[j][i]=max(Str_maze[j][i-1],Str_maze[j-1][i])+1
                    elif j==0 and Str_maze[j][i-1]!=-1:
                        Str_maze[j][i]=Str_maze[j][i-1]+1
                else:
                    Str_maze[j][i]=-1
        else:
            for j2 in range(n-1,-1,-1):
                if L[j2][i]!="#":
                    if j2<n-1 and (Str_maze[j2+1][i]!=-1 or  Str_maze[j2][i-1]!=-1):
                        Str_maze[j2][i]=max(Str_maze[j2+1][i],Str_maze[j2][i-1])+1
                    elif j2==n-1 and Str_maze[j2][i-1]!=-1:
                        Str_maze[j2][i]=Str_maze[j2][i-1]+1
                else:
                    Str_maze[j2][i]=-1
        

    return Str_maze[n-1][n-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )
