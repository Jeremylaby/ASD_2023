from egzP5atesty import runtests 

def inwestor ( T ):
    n=len(T)
    LS=[-1 for _ in range(n)]
    RS=[n for _ in range(n)]
    stack=[-1,0]
    for i in range (1,n):
        while stack[-1]!=-1 and T[stack[-1]]>T[i]:
            RS[stack[-1]]=i
            stack.pop()
        if T[i]==T[i-1]:
            LS[i]=LS[i-1]
        else:
            LS[i]=stack[-1]
        stack.append(i)
    maks=0
    for i in range(n):
        maks=max(maks,(RS[i]-LS[i]-1)*T[i])
        


    return maks

runtests ( inwestor, all_tests=True)