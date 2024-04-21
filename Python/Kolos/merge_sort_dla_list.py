class Node:

    def __init__(self,v):
        self.next=None
        self.val=v
def cut(w):
    i=w
    j=w.next
    if j is None:
        return None,None
    while j.next!=None and j.val<=j.next.val:
        j=j.next
    #print(i.next.val,"c")
    i=i.next
    w.next=j.next
    j.next=None
    #print(i.val,"m")
    #display(i)
    return i,j
def merge(p1,p2):
    h=Node(None)
    t=h
    #print(p2.val,"3")
    #display(p1)
    #display(p2)
    while p1 and p2:
        if p1.val <=p2.val:
            t.next=p1
            p1=p1.next
            t=t.next
        else:
            t.next=p2
            p2=p2.next
            t=t.next
    while p1:
        t.next=p1
        p1=p1.next
        pr=t
        t=t.next
    while p2:
        t.next=p2
        p2=p2.next
        pr=t
        t=t.next
    t.next=None
    #display(h)
    #print(t.val,"r")
    return h.next,t
def merge_sort (h):
    p=h

    t=h
    while t.next.next is not None:
        t=t.next
    i=0
    while True:
        print(t.val,"1")
        lh,ltt=cut(h)
        rh,rt=cut(h)
        print("rh",rh,"2")
        if rh is None:
            h.next=lh
            ltt.next=None
            return
        if t==rt:
            t=h
        mh,mt=merge(rh,lh)
        t.next=mh
        t=mt

        #print(mt.val)
        #display(h)
def inwersja(t):
    n=len(t)
    i=0
    j=1
    num=0
    if n==1:
        return 0
    while i<n-1:
        if j==n:
            i+=1
            j=i+1
        elif t[j]<t[i]:
            j+=1
            num+=1
        else:
            j+=1

    return num