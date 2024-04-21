from egzP4btesty import runtests 

class Node:
  def __init__(self, key, parent):
    self.left = None
    self.right = None
    self.parent = parent
    self.key = key
    self.x = None
def max_prev(root):
  curr=root
  while curr.right:
    curr=curr.right
  return curr

def find_prev(root):
  if root.left:
    return max_prev(root.left)
  next=root
  prev=root.parent
  while prev and next==prev.left:
    next=prev
    prev=prev.parent
  return prev

def min_next(root):
  while root.left:
    root=root.left
  return root

def find_next(root):
  if root.right:
    return min_next(root.right)
  next=root
  prev=root.parent
  while prev and next==prev.right:
    next=prev
    prev=prev.parent
  return prev
   
   
def sol(root, T):
  suma=0
  for i in T:
    a=find_prev(i)
    b=find_next(i)
    if a!=None and b!=None and a.key+b.key==i.key*2:
      suma+=i.key
  return suma
    
runtests(sol, all_tests = True)