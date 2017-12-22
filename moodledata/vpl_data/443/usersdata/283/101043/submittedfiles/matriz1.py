# -*- coding: utf-8 -*-
m=int(input('Digite o numero de linhas: '))
n=int(input('Digite o numero de colunas: '))
a=[]

for i in range(0,m,1):
    l=[]
    for j in range(0,n,1):
        l.append(int(input('Digite um elemento: ')))
        a.append(l)
b=[]
for g in range(m-1,-1,-1):
    t=[]
    for h in range(n-1,-1,-1):
        t.append(a[g][h])
        b.append(t)
print(b)
