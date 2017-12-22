# -*- coding: utf-8 -*-
import numpy as np
#ENTRADAS
ordem=int(input('Digite a dimensão n da matriz: '))
x=int(input("Digite a linha do número: "))
y=int(input("Digite a coluna do número: "))
matriz=np.zeros((ordem,ordem))
for i in range(0,ordem,1):
    for j in range(0,ordem,1):
        matriz[i,j]=int(input("Digite os valores da matriz: "))
        
        
#EXECUÇÃO
#SOMANDO A LINHA
i=x
soma=0
for j in range(0,ordem,1):
    if j!=y:
        soma=soma+matriz[i,j]
    
#SOMANDO A COLUNA
j=y
soma1=0
for i in range(0,ordem,1):
    if i!=x:
        soma1=soma1+matriz[i,j]
        
peso=soma+soma1
print(peso)

