#mamy tablice A wypełnioną liczbami naturalnymi mamy jakąś zadaną sume T mamy sprawdzić czy z tablicy A jesteśmy wstanie stworzyć
#tablice B o sumie elementów równej T
def find_sum(A,T):
    T_tab=[False for _ in range(T+1)]
    T_tab[0]=True
    pos=1
    for i in range(len(A)):
        for j in range(pos):
            if T_tab[j] and j+A[i]<=T:
                T_tab[j+A[i]]=True
                max_pos=max(pos,j+A[i])
                if T_tab[-1]:
                    return True
        pos=max_pos
    return False
A=[1,2,3,4,5,6,7,8,9,10,23,40,50]
print(find_sum(A,72))
def find_sum2(A,T):
    n=len(A)
    T_tab=[[False]*(T+1) for _ in range(T+1)]
    for i in range(n+1):
        e=2
#najdłóższy wspólny podciąg w 2 zadanych tablicach o tej samej długości 
# cw. 4
def find_longest_squence(A,B):
    n=len(A)
    F=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if j-1>=0 and i-1>=0:
                F[i][j]=max(F[i-1][j],F[i][j-1])
                if A[i]==B[j]:
                    F[i][j]=max(F[i][j],F[i-1][j-1]+1)
            elif i-1>=0:
                F[i][j]=max(F[i][j],F[i-1][j])
                if A[i]==B[j]:
                    F[i][j]+=1
            elif j-1>=0:
                F[i][j]=max(F[i][j],F[i][j-1])
                if A[i]==B[j]:
                    F[i][j]+=1
            else:
                if A[i]==B[j]:
                    F[i][j]+=1
    S=path_F(F,B)
    return F[n-1][n-1],F,S
def path_F(F,B):
    S=[]
    i=len(F)-1
    j=len(F)-1
    while i >0 and j>0:
        if F[i-1][j] == F[i][j-1]:
            if F[i][j-1]!=F[i][j]:
                S.append(B[j])
                i-=1
                j-=1
            elif F[i-1][j]==F[i][j]:
                i-=1
            else:
                j-=1
                
        elif F[i-1][j]==F[i][j]:
            i-=1
        elif F[i][j-1]==F[i][j]:
            j-=1
    if F[i][j]!=0:
        S.append(B[j])
    S=S[::-1]
    return S

A=["a","b","e","t","s","c","w","b","d"]
B=["c","b","q","n","m","a","b","c","d"]
longest,F,S=find_longest_squence(A,B)
print(longest)
print(S)
for i in range(len(F)):
    print(F[i])

            
#mamy ciag macierzy, znamy ich rozmiary, szukamy kolejnosci
#w jakiej mamy pomnozyc macierze tak by
#liczba operacji podczas mnozenia macierzy byla jak najmniejsza
#innymi slowy jak najmniejszy koszt

#mamy szachownice liczb wymiernych idziemy w prawo lub w dół nie cofamy sie mamy znaleźć koszt najtańszej drogi 
def zas_ta_szachownica(T):
    n=len(T)
    T_cost=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i>0 and j>0:
                T_cost[i][j]=min(T_cost[i-1][j]+T[i][j],T_cost[i][j-1]+T[i][j])
            elif i>0:
                T_cost[i][j]=T_cost[i-1][j]+T[i][j]
            elif j>0:
                T_cost[i][j]=T_cost[i][j-1]+T[i][j]
    path=path_T_cost(T_cost,T)
    return T_cost[n-1][n-1],path
def path_T_cost(T_cost,T):
    path=[]
    n=len(T_cost)
    i,j=n-1,n-1
    while i>0 or j>0:
        if i>0 and T_cost[i-1][j]==T_cost[i][j]-T[i][j]:
            path.append((i,j))
            i-=1
        elif j>0 and T_cost[i][j-1]==T_cost[i][j]-T[i][j]:
            path.append((i,j))
            j-=1
    path.append((0,0))
    path=path[::-1]
    return path

Szachwnica=[[0,-1,-1,3,4,8],
            [4,1,2,5,6,8],
            [2,1,3,2,7,8],
            [4,2,6,3,2,1],
            [5,2,4,5,2,1],
            [1,1,1,1,1,1]]
print(zas_ta_szachownica(Szachwnica))