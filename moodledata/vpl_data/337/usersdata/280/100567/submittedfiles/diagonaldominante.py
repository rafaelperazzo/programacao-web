# -*- coding: utf-8 -*-
import numpy as np
n=int(input("Digite n: "))
matriz=np.empty([n,n])
zero=np.empty([n,n])
cont=0

for i in range(0,n,1):
    for j in range(0,n,1):
        matriz[i][j]=int(input("Insira um valor: "))
        
        
for i in range(0,n,1):
    for j in range(0,n,1):
        zero[i][j]=matriz[i][j]
        
for i in range(0,n,1):
    zero[i][i] = 0
    
print(matriz)
print(zero)
    
for i in range(0,n,1):
    if matriz[i][i] > sum(zero[i]):
        cont=cont+1


if cont==n:
    print("SIM")
else:
    print("NAO")
    

