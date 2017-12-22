# -*- coding: utf-8 -*-
import numpy as np
a=[]
b=int(input('digite a ordem da matriz: '))
while not b>=3:
    b=int(input('digite a ordem da matriz: '))
    
for i in range(0,b,1):
    linha=[]
    for j in range(0,b,1):
        linha.append(int(input('digite os elementos: ')))
    a.append(linha)
c=np.empty([b,b])
for i in range(0,b,1):
    for j in range(0,b,1):
        c[i][j]=a[i][j]
    
soma= sum(a[0])+sum(c[0])-2*(a[i][j])
for i in range(0,b,1):
    for j in range(0,b,1):
        if soma>sum(a[i])+sum(c[j])-2*(a[i][j]):
            soma=soma
        else:
            soma=sum(a[i])+sum(c[j])-2*(a[i][j])

print(int(soma))