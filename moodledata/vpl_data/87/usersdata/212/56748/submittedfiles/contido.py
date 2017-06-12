# -*- coding: utf-8 -*-
n=int(input('digite o tamanho da lista a:'))
m=int(input('digite o tamanho da lista b:'))
a=[]
b=[]
cont=0
for i in range(0,n,1):
    v=int(input('digite um número para lista a:'))
    a.append(v)    
for o in range(0,m,1):
    n=int(input('digite um número para lista b:'))
    b.append(n)
for t in range(0,n,1):
    for q in range(0,m,1):
        if a[t]==b[q]:
            cont=cont+1
print(cont)