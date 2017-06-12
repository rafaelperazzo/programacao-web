# -*- coding: utf-8 -*-
n=int(input('digite o numero de elemetos da lista:'))
x=[]
for i in range(1,n+1,1):
    y=float(input('digite um elemento:'))
    x.append(y)
soma=0
for i in range(0,n,1):
    soma=soma+x[i]
media=soma/n
print('%.2f'%lista[0])
print('%.2f'%lista[len(a)-1])
print('%.2f'%media)
print(x)