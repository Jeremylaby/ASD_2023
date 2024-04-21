def Relax(par,d,i,j,G):
    if d[j]>d[i]+G[j][k]:
        d[j]=d[i]+G[j][k]
        par[j]=i
        return True
    return False

def Belman_Ford(G,v):# dla macierzy sąsiedztwa 
    n=len(G)
    d=[inf]*n
    parent=[None]*n
    d[v]=0
    for i in range (n):
        B=False
        for j in range (n):
            for k in range(n):
                if G[j][k]:
                    B|=Relax(parent,d,j,k,G)
        if i ==n-1 and B: return d,parent,False 
    else : return d,parent,True