# -*- coding: utf-8 -*-

import numpy as np
m=int(input("Digite a ordem da matriz:"))
matri=np.empty([m, m])
for i in range (m):
  for j in range (m):
    matri[i][j]=(int(input("Digite um elemento para a matriz:")))
    
    

a=[]

for k in range (m):
  somaCol=0
  for f in range (m):
    somaCol=matri[f][k]+somaCol
  a.append(somaCol)
 
b=[] 
  
for p in range (m):
  b.append(sum(matri[p]))
  
c=[]
for h in range (m):
  for o in range (m):
    c.append(b[h]+a[o]-(2*matri[p][o]))
  

  
print(max(c))
