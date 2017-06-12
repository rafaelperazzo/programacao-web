# -*- coding: utf-8 -*-
n=int(input('Digite n:'))
a=[]
soma=0
for i in range(0,n,1):
    a.append(int(input('Elemento da lista: ')))
    soma=soma+a[i]
b=a[0]
c=a[n-1]
m=soma/2
print(b)
print(c)
print(m)
print(a)
    

