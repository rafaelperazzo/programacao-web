# -*- coding: utf-8 -*-
import numpy as np
d=int(input("digite o valor da dimenão:"))
linha=int(input("digite a linha desejada"))
coluna=int(input("digite a coluna desejada"))
matriz=np.zeros( (d,d) )
for i in range (0,matriz.shape[0],1):
    for j in range (0,matriz.shape[1],1):
        matriz[i,j]=float(input("digite o elemento da matriz requerido"))
i=linha
soma=0
for j in range(0,matriz.shape[1],1):
    soma=soma+matriz[i,j]
j=coluna    
for i in range(0,matriz.shape[0],1):
    soma=soma+matriz[i,j]
total=soma-(2*matriz[linha,coluna])
print("%d será o valor total" %total)