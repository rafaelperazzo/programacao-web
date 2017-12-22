# -*- coding: utf-8 -*-

import numpy as np

n=int(input("Insira n: "))
while n < 3:
    n=int(input("Insira n: "))

matriz=np.empty([n,n])
trans=np.empty([n,n])

for i in range (0,n,1):
    for j in range (0,n,1):
        matriz[i][j]=int(input("Insira um valor: "))

for i in range (0,n,1):
    for j in range (0,n,1):
        trans[i][j]=matriz[j][i]

somlin=np.empty([1,n])
somcol=np.empty([1,n])

for i in range (0,n,1):
    somlin[0]=sum(matriz[i])
    
for i in range (0,n,1):
    somcol[0]=sum(trans[i])
    
contlin=np.empty([1,n])
contcol=np.empty([1,n])

for i in range (0,n,1):
    contlin[i]=somlin.count(somlin[i])
    
for i in range (0,n,1):
    contcol[i]=somcol.count(somcol[i])
    
max=0
lin=0
col=0

for i in range (0,n,1):
    if contlin[i] != 1:
        max=somcol[i]
        break
 
for i in range (0,n,1):
    if contlin[i] == 1:
        lin=i
        break

for i in range (0,n,1):
    if contcol[i] == 1:
        col=i
        break
    
numatual=matriz[lin][col]

matriz[lin][col]=0

numnovo=max-sum(matriz[lin])

print(numatual)
print(numnovo)
    
    



