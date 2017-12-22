# -*- coding: utf-8 -*-
import numpy as np
m=int(input("Digite m: "))
n=int(input("Digite n: "))
matriz=np.empty([m,n])
mat1=np.empty([m,n])
mat2=np.empty([m,n])

for i in range(0,m,1):
    for j in range(0,n,1):
        matriz[i][j]=int(input("Digite um valor: "))
        
for i in range(0,m,1):
    for j in range(0,n,1):
        mat1[i][j]=matriz[i][n-1-j]

for i in range(0,n,1):
    for j in range(0,m,1):
        mat2[j][i]=mat1[m-1-j][i]

print(matriz)
print(mat1)
print(mat2)