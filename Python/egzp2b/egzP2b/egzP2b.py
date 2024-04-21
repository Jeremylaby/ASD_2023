from egzP2btesty import runtests
from math import log10
import bisect
class Node:
    def __init__(self):
        self.val=0
        self.left=None
        self.right=None
def add(root,new):
    curr=root
    while True:
        if len(new.val)>=len(curr.val) and curr.right==None:
            curr.right=new
            return
        elif len(new.val)<len(curr.val) and curr.left==None:
            curr.left=new
            return
        elif len(new.val)>=len(curr.val):
            curr=curr.right
        elif len(new.val)<len(curr.val):
            curr=curr.left
                 
def build_BST(root,string):
    while string!="":
        if string[-1]=="1":
            root.val+=1
            string=string[:-1]
            if root.right==None:
                root.right=Node()
            root=root.right
        else:
            root.val+=1
            string=string[:-1]
            if root.left==None:
                root.left=Node()
            root=root.left
    root.val+=1
    return
def find_num_of_sufix(root,string):
    while string!="":
        if string[-1]=="1":
            string=string[:-1]
            root=root.right
        else:
            string=string[:-1]
            root=root.left
    return root.val
def radixSort(tab,x):
    while x!=-1:
        output_0=[]
        output_1=[]
        for i in tab:
            if len(i)<=x:
                output_0=[i]+output_0
            elif i[x]=="1":
                output_1.append(i)
            else:
                output_0.append(i)
        tab=output_0+output_1
        x-=1
    return tab
def kryptograf( D, Q ):
    maks=0
    for i in range(len(D)):
        D[i]=D[i][::-1]
        maks=max(len(D[i]),maks)
    for i in range(len(Q)):
        Q[i]=Q[i][::-1]
    D=radixSort(D,maks)
    sum=0
    for i in Q:
        lo=bisect.bisect_left(D,i)
        hi=bisect.bisect_right(D,i+"2")
        sum+=log10(hi-lo)
    return sum


"""def kryptograf( D, Q ):    
    root=Node()
    for i in D:
        build_BST(root,i)
    sum=0
    for j in Q:
        num=find_num_of_sufix(root,j)
        sum+=log10(num)
    return sum"""

    #tutaj proszę wpisać własną implementację

# Zmień all_test na:
# 0 - Dla małych testów
# 1 - Dla złożoności akceptowalnej
# 2 - Dla złożoności dobrej
# 3 - Dla złożoności wzorcowej
runtests(kryptograf, all_tests = 3)