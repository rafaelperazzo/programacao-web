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
    if sum(a[i])>=1:
        c.append(i)
        break
for i in range(m-1,-1,-1):
    if sum(a[i])>=1:
        c.append(i)
        break
#LIMITES LATERAIS
lat=[]
for i in range(0,m,1):
    for j in range(0,n,1):
        if a[i][j]==1:
            lat.append(j)

x=sorted(lat) #x[0]x[n-1]

c1=int(c[0])
c2=int(c[1])
x1=int(x[0])
x2=int(x[n-1])
n=[]
for i in range(c[0],c[1],1):
    for j in range(x[0],x[n-1],1):
        n.append(a[i][j])


print(n)