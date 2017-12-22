# -*- coding: utf-8 -*-
n = int(input('Quantidade de números: '))
x = []
y = []
for i in range(0,n,1):
    x.append(int(input('Digite os números: ')))
for i in range(n):
    y.append(x[i//2==0])
print (x)
print (y)