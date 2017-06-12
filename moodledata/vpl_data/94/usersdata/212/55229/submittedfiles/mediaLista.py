# -*- coding: utf-8 -*-
n=int(input('digite o numero de elementos da lista:'))
a=[]
for i in range(0,n,1):
    v=float(input('digite um valor:'))
    a.append(v)
soma=0
for cont in range(0,n,1):
    soma=soma+a[cont]
m=soma/n
print('%.2f'%a[0])
print('%.2f'%a[n-1])
print('%.2f'%m)
for c in range(0,n,1):
    print(a[c])