# -*- coding: utf-8 -*-
from __future__ import division
#entrada
def lecker(lista):
    cont=0
    for i in range(0, len(lista),1):
        if i==0:
            if x[i]>x[i+1]:
                cont=cont+1
        elif i==(len(x)-1):
            if x[i]>x[i-1]:
                cont=cont+1
        else:
            if (x[i]>x[i-1])and(x[i]>x[i+1]):
                cont=cont+1
    return lecker
#processamento
a[]
b[]
n=int('digite a quantidade de elementos:')
for i in range(0,n,1):
    a.append(input('digite um elemento:')
for i in range(0,n,1):
    b.append(input('digite um elemento:')
lecker_a=lecker(a)
lecker_b=lecker(b)
#saida
    if cont==1:
        print('s')
    else:
        print('n')
            

