class Node:
  def __init__(self, wyborcy, koszt, fundusze):
    self.next = None
    self.wyborcy = wyborcy 
    self.koszt = koszt 
    self.fundusze = fundusze 
    self.x = None   
wyb1okr1 = Node(3, 8, 15)
wyb1okr2 = Node(2, 7, 15)
wyb1okr3 = Node(4, 5, 15)
wyb1okr1.next = wyb1okr2
wyb1okr2.next = wyb1okr3
wyb2okr1 = Node(4, 7, 8)
wyb2okr2 = Node(5, 2, 8)
wyb2okr1.next = wyb2okr2
wyb3okr1 = Node(3, 5, 10)
wyb3okr2 = Node(3, 5, 10)
wyb3okr1.next = wyb3okr2
T = [wyb1okr1, wyb2okr1, wyb3okr1]
def wybory(T):
  sum=0
  for i in T:
    tab=[]
    x=-1
    while i!=None:
      i.x=x+1
      val=i.wyborcy
      weight=i.koszt
      x=i.x
      n=i.fundusze
      tab.append([0 for _ in range(n)])
      
      for j in range(n):
        if x==0 and weight-1>j:
          tab[x][j]=0
        elif x==0 and weight-1<=j:
          tab[x][j]=val
        elif weight-1>j:
          tab[x][j]=tab[x-1][j]
        elif j-weight>=0:
          tab[x][j]=max(tab[x-1][j],tab[x-1][j-(weight)]+val)
        else:
          tab[x][j]=max(tab[x-1][j],val)
      i=i.next
      print(tab)
    print(tab[x][n-1])
    sum+=tab[x][n-1]
        

    #tutaj proszę wpisać własną implementację
  return sum
print(wybory(T))