maks_x=0
  n=len(P)
  P=sorted(P, key=lambda x: (x[0],x[1]))
  MAKS=0
  for i in range (n):
    suma=0
    for j in range(n):
      x1,y1=P[i]
      x2,y2=P[j]
      if i!=j and x1>x2 and y1>y2:
        suma+=1
    MAKS=max(MAKS,suma)
  return MAKS
  n=len(P)
  for i in range(n):
    for j in range(i):
      x1,y1=P[i]
      x2,