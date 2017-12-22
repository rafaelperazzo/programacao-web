# -*- coding: utf-8 -*-
n=int(input('Quantidade de termos da lista a: '))
a=[]
m=int(input('Quantidade de termos da lista a: '))
b=[]
for i in range(n):
    a.append(int(input('Termo da lista a: ')))
for i in range(m):
    b.append(int(input('Termo da lista b: ')))
cont=0
if len(a)<len(b):
    for i in range(n):
        for j in range(m):
            if a[i]==b[j]:
                cont+=1
elif len(b)<len(a):
    for i in range(m):
        for j in range(n):
            if b[i]==a[j]:
                cont+=1
print(cont)