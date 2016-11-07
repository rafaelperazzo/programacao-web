# -*- coding: utf-8 -*-
from __future__ import division

n= int(input('Digite o valor n: '))
x= []
y= []

for i in range(0, n, 1):
    x.append(input('Digite um valor: '))
for i in range(0, n, 1):
    y.append(input('Digite um valor: '))

cont= 0
for i in range(0, len(x), 1):
    if len(i)==0:
        if x[i]>(x[i+1]):
            cont = cont+ 1
    elif len(i)==len(x):
        if x
        
        