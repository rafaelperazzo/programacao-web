# -*- coding: utf-8 -*-
import numpy as np

def numlinha(matriz,valorsoma):
    for i in range(0,n,1):
        soma=0
        for j in range(0,n,1):
            soma=soma+matriz[i,j]
        if valorsoma!=soma:
            return(i)
    
def numcoluna(matriz,valorsoma):
    for j in range(0,n,1):
        soma=0
        for i in range(0,n,1):
            soma=soma+matriz[i,j]
        if valorsoma!=soma:
            return(j)
            
def valorsoma(matriz):
    x=0
    y=0
    z=0
    for i in range(0,n-2,1):
        for j in range(0,n,1):
            x=x+matriz[i,j]
            y=y+matriz[i+1,j]
            z=z+matriz[i+2,j]
        if x==y:
            return(x)
        if x==z:
            return(x)
        if y==z:
            return(y)
            
n=0
while n<3:
    n=int(input('Digite a dimensão da matriz: '))

matriz=np.zeros((n,n))

for i in range(0,n,1):
    for j in range(0,n,1):
        matriz[i,j]=int(input('Digite os elementos da matriz: '))
valor=valorsoma(matriz)
linha=numlinha(matriz,valor)
coluna=numcoluna(matriz,valor)

soma=0
for i in range(0,n,1):
    soma=soma+matriz[linha,i]

laura=matriz[linha,coluna]
original=valor-(soma-laura)

print(original)
print(laura)

