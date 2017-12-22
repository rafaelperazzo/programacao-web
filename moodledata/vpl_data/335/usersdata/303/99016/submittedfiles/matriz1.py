# -*- coding: utf-8 -*-
a=[]
c=[]
m=int(input('Digite a quantidade de linhas: '))
n=int(input('Digite a quantidade de colunas: '))
for i in range(0,m,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input('Digite o termo: ')))
    a.append(linha)
for i in range(0,m,1):
    if sum(a[i])>1:
        c.append(a[i])
        break
for i in range(m-1,-1,-1):
    if sum(a[i])>1:
        c.append(a[i])
        break
    
print(c)