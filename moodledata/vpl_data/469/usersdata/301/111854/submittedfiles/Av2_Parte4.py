# -*- coding: utf-8 -*-
a=[]
n=int(input('digite o tamanho da matriz:  '))
for i in range(0,n,1):
    linhas=[]
    for j in range(0,n,1):
        linhas.append(int(input('digite o valor das linhas:  ')))
    a.append(linhas)
b=[]
for i in range(0,n,1):
    s1=0
    for j in range(0,n,1):
        s1+=a[i][j]
    a.append(b)
print(s1)
c=[]
for j in range(0,n,1):
    s2=0
    for i in range(0,n,1):
        s2+=a[j][i]
    a.append(c)
print(s2)