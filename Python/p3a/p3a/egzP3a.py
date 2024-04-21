from egzP3atesty import runtests
from math import inf

class Node:
  def __init__(self, wyborcy, koszt, fundusze):
    self.next = None
    self.wyborcy = wyborcy 
    self.koszt = koszt 
    self.fundusze = fundusze 
    self.x = None

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
    sum+=tab[x][n-1]
        

    #tutaj proszę wpisać własną implementację
  return sum

runtests(wybory, all_tests = True)