# -*- coding: utf-8 -*-
import math
a=[]
b=[]
n=int(input('Digite a quantidade de elementos de a: '))
m=int(input('Digite a quantidade de elementos de b: '))
for i in range(n):
    a.append(int(input('Digite o elementoa: ')))
for j in range(m):
    b.append(int(input('Digite o elementob: ')))
soma=0
for j in range(0,n,1):
    for i in range(0,m,1):
        if b[j]==a[i]:
            soma=+1
        if b[0]==a[1]:
            soma=+1
        
print (soma)
    
    