from math import inf

def problem_plecakowy_rekurencyjny(S,W,P):
    D=[[None]*(S+1) for _ in range(len(W))]
    def f(D,S,W,P,i):
        if S<0:
            return -inf
        if i>=len(P):
            return 0
        if D[i][S]!=None:
            return D[i][S]
        d1=f(D,S-W[i],W,P,i+1)+P[i]
        d2=f(D,S,W,P,i+1)
        D[i][S]=max(d1,d2)
        return D[i][S]
    return f(D,S,W,P,0)
item_list=[(1,50),(2,60),(4,20),(10,200),(2,70)]
W=[4,2,4,10,5]
P=[50,60,20,200,70]
print(problem_plecakowy_rekurencyjny(12,W,P))