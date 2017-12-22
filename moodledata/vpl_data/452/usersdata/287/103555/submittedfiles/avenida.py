# -*- coding: utf-8 -*-
n=int(input('digite o valor de n'))
m=int(input('digite o valor de m'))
matriz=[]
for i in range(0,n,1):
    linhas=[]
    i=int(input("qual o valor da quadra %d,%d?" %(i+1,j+1)))
    linhas.append(i)
    matriz.append(linhas)
    for j in range(0,m,1):
        j=int(input("qual o valor da quadra %d,%d?" %(i+1,j+1)))
        matriz.append(j)    
print(matriz)
    

