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


somlin=[]
somcol=[]

for i in range (0,n,1):
    somlin.append(sum(matriz[i]))
    
for i in range (0,n,1):
    somcol.append(sum(trans[i]))


contlin=[]
contcol=[]

for i in range (0,n,1):
    contlin.append(somlin.count(somlin[i]))
    
for i in range (0,n,1):
    contcol.append(somcol.count(somcol[i]))

    
max=0
lin=0
col=0

for i in range (0,n,1):
    if contlin[i] != 1:
        max=somlin[i]
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

print(int(numnovo))
print(int(numatual))
    
    



