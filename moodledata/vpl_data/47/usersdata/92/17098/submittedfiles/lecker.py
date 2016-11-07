# -*- coding: utf-8 -*-
from __future__ import division

n= int(input('Digite o valor n: '))
x= []
y= []

for i in range(0, n, 1):
    x.append(input('Digite um valor: '))
for i in range(0, n, 1):
    y.append(input('Digite um valor: '))

def lecker(x):

    cont= 0
    for i in range(0, len(x), 1):
        if i==0:
            if x[i]>(x[i+1]):
                cont = cont+ 1
        elif i==len(x):
            if x[i]>x[i-1]:
                cont= cont+ 1
        else:
            if x[i]>x[i-1] and x[i]>x[i+1]:
                cont= cont+ 1
    if cont==0:
        return False
    else:
        return True

if lecker(x):
    print('S')
else:
    print('N')

if lecker(y):
    print('S')
else:
    print('N')






        
        