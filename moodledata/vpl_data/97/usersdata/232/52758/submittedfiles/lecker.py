# -*- coding: utf-8 -*-
from __future__ import division
def lecker(a):
    cont=0
    for i in range (0,len(a),1):
        if i==0:
            if a[i]>a[i+1]:
                cont=cont+1
        elif i==(len(a)-1):
            if a[i]>a[i-1]:
                cont=cont+1
        else:
            if a[i]>a[i+1] an a[i]>a[i-1]:
                cont=cont+1
    if cont==0:
        return ('N')
    else:
        return ('S')


a=[ ]
b=[ ]
n1=int(input('Digite o número de elementos da lista a: '))
n2=int(input('Digite o número de elementos da lista b: '))
for i in range (1,n,1):
    num=int(input('Digite o elemento da lista: '))
    a.append(num)




























