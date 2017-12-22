# -*- coding: utf-8 -*-
n=int(input('N: '))
m=int(input('M: '))
matriz=[]
for i in range(0,n-1,1):
    linhas=[]
    for j in range(0,m-1,1):
        i=int(input("qual o valor da quadra %d,%d?" %(i+1,j+1)))
        j=int(input("qual o valor da quadra %d,%d?" %(i+1,j+1)))
        linhas.append(j)
        matriz.append(linhas)
print(matriz)
    

