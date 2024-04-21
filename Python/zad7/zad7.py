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
    Walk_down=[-1 for _ in range(n)]
    Walk_up=[-1 for _ in range(n)]
    for i in range(1,n):
        
        for j in range(n):
            j2=(n-1)-j
            if L[j][i]!="#":
                if j>0 and (Str_maze[j][i-1]!=-1 or Walk_down[j-1]!=-1):
                    Walk_down[j]=max(Str_maze[j][i-1],Walk_down[j-1])+1
                elif j==0 and Str_maze[j][i-1]!=-1:
                    Walk_down[j]=Str_maze[j][i-1]+1
            else:
                Walk_down[j]=-1
            if L[j2][i]!="#":
                if j2<n-1 and (Walk_up[j2+1]!=-1 or  Str_maze[j2][i-1]!=-1):
                    Walk_up[j2]=max(Walk_up[j2+1],Str_maze[j2][i-1])+1
                elif j2==n-1 and Str_maze[j2][i-1]!=-1:
                    Walk_up[j2]=Str_maze[j2][i-1]+1
            else:
                Walk_up[j2]=-1
        for l in range(n):
            Str_maze[l][i]=max(Walk_down[l],Walk_up[l])
        

    return Str_maze[n-1][n-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )
