# -*- coding: utf-8 -*-
x=int(input('Digite o tamanha da primeira lista:'))
y=int(input('Digite o tamanho da segunda lista:'))
a=[]
b=[]
cont=0
for r in range(0,n,1):
    v=int(input('Digite um valor:'))
    a.append(v)
for p in range(0,m,1):
    n=int(input('Digite um número:'))
    b.append(n)
print(a)
print(b)
for l in range(0,len(a),1):
    for w in range(0,len(b),1):
        if a[l]==b[w]:
            cont=cont+1
print(cont)

