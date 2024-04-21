from egzP4atesty import runtests 
#ogólnie ten algorytm jest defakto problemem najdłuższego podciągu po 2 współrzędnych mostu
# dla lepszej złożoności stawiam że trzeba wykorzystać binsearcha
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        self.x=0
def insert(T,i,node):
    curr=0
    value=T[i][1]
    while True:
        if value>=node.val:
            if node.right==None:
                node.right=Node(T[i][1])
                curr+=1
                return curr+1
            node=node.right
            curr+=1
        else:
            if node.left==None:
                node.left=Node(T[i][1])
                return curr+1
            node=node.left


def mosty ( T ):
    T.sort(key=lambda x:(x[0],x[1]))
    start=Node(T[0][1])
    start.x=1
    for i in range(1,len(T)):
        curr=0
        start.x=max(insert(T,i,start),start.x)


    return start.x

runtests ( mosty, all_tests=True )