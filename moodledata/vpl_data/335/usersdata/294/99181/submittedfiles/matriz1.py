# -*- coding: utf-8 -*-
matriz=[]
m= int(input('Digite o numero de linhas: '))
n= int(input('Digite o numero de colunas: '))
for i in range (0,m,1):
    linha=[]
    for j in range (0,n,1):
        linha.append(int(input('Digite um binario[0,1]: ')))
    matriz.append(linha)

c=[]
for i in range(0,m,1):
    if sum(a[i]>=1:
        c.append(i)
        break
for i in range (m-1,-1,-1):
    if sum(a[i])>=1:
        c.append(i)
        break
    
#Laterais
lat=[]
for i in range(0,m,1):
    forj in range 