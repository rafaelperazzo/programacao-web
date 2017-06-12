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
            if a[i]>a[i+1] and a[i]>a[i-1]:
                cont=cont+1
    if cont==1:
        return ('S')
    else:
        return ('N')


a=[ ]
b=[ ]
n=int(input('Digite o número de elementos da lista: '))
for i in range (1,n+1,1):
    num1=int(input('Digite o elemento da lista a: '))
    a.append(num1)
for i in range (1,n+1,1):
    num2=int(input('Digite o elemento da lista b: '))
    b.append(num2)

print(lecker(a))
print(lecker(b))