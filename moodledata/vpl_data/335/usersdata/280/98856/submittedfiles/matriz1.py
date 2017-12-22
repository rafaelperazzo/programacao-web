# -*- coding: utf-8 -*-
import numpy as np
n=int(input("Digite n: "))
m=int(input("Digite m: "))
matriz=np.empty([n,m])
matriztrans=np.empty([m,n])

for i in range(0,n,1):
    for j in range(0,m,1):
        matriz[n][m]=("Digite n: ")

for i in range(0,n,1):
    for j in range(0,m,1):
        matriztrans[i][j]=matriz[j][i]

contlin1=0
contlin2=0
contcol1=0
contcol2=0

for i in range(0,n,1):
    if sum(matriz[i]) != 0:
        contlin1=contlin1+i
        break

for i in range(n-1,-1,-1):
    if sum(matriz[i]) != 0:
        contlin2=contlin2+i
        break

for i in range(0,m,1):
    if sum(matriztrans[i]) != 0:
        contcol1=contcol1+i
        break
        
for i in range(m-1,-1,-1):
    if sum(matriztrans[i]) != 0:
        contcol2=contcol2+i
        break

recorte=np.empty([contlin2-contlin1+1,contcol2-contcol1+1])

print(matriz)
print(matriztrans)
print(recorte)

