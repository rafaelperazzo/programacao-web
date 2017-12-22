# -*- coding: utf-8 -*-
n = int(input('Quantidade de números: '))
x = []
y = []
z = []
for i in range(0,n,1):
    x.append(int(input('Digite os números: ')))
    y.append(i//2==0)
print (x)
print (y)