# -*- coding: utf-8 -*-
a=[]
n=int(input('digite o tamanho da matriz:  '))
for i in range(0,n,1):
    linhas=[]
    for j in range(0,n,1):
        linhas.append(int(input('digite o valor das linhas:  ')))
    a.append(linhas)
b=[]
s1=0
for i in range(0,n,1):
    
    for j in range(0,n,1):
        s1=+a[i][j]
    b.append(s1)
a.append(b)
print(s1)
c=[]
for j in range(0,n,1):
    s2=0
    for j in range(0,n,1):
        s2=+a[i][j]
    c.append(s2)
print(s2)