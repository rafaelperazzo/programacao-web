# -*- coding: utf-8 -*-
n=int(input('digite o numero de elementos de a:'))
m=int(input('digite o numero de elementos de b:'))

a=[]
b=[]
for i in range(1,n+1,1):
    valor=float(input('digite o valor:'))
    a=a.append(valor)
print(a)