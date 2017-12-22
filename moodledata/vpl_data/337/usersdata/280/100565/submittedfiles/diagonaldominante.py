# -*- coding: utf-8 -*-
import numpy as np
n=int(input("Digite n: "))
matriz=np.empty([n,n])
diag=np.empty([1,n])
cont=0

for i in range(0,n,1):
    for j in range(0,n,1):
        matriz[i][j]=int(input("Insira um valor: "))
        
        
for i in range(0,n,1):
    diag[0][i]=matriz[i][i]
    
print(matriz)
print(diag)
    
for i in range(0,n,1):
    if diag[0][i] > sum(matriz[i]):
        cont=cont+1


if cont==n:
    print("SIM")
else:
    print("NAO")
    

