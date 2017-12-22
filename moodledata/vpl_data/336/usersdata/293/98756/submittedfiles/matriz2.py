# -*- coding: utf-8 -*-
import numpy as np
soma_secun=0
soma_princ=0
soma_linhas=0
soma_colunas=0

n=int(input("Digite o número de linhas da matriz: "))
while(True):
    if n<2:
        n=int(input("Digite o número de linhas da matriz: "))
    else:
        break
    
matriz= np.empty([n,n])

for i in range(0,n,1):
    for j in range(0,n,1):
        matriz[i,j]= int(input("Digite o elemento da %dª linhas e da %dª coluna, respectivamente: "%(i+1,j+1)))
for i in range(0,n,1):
    for j in range(0,n,1):
        matriz[i,j]= soma_linhas + matriz[i,j]
for j in range(0,n,1):
    for i in range(0,n,1):
        matriz[i,j]= soma_colunas + matriz[i,j]
for i in range(0,n,1):
    for j in range(0,n,1):
        if i+j==n-1:
            matriz[i,j]= soma_secun + matriz[i,j]
        elif i==j:
            matriz[i,j]= soma_princ + matriz[i,j]

if soma_secun==soma_princ==soma_colunas==soma_linhas:
    print("S")
else:
    print("N")
    

       

