# -*- coding: utf-8 -*-
from __future__ import division
def lecker(lista):
    c=0
    for in in range(0,len(lista)-1,1):
        if i==0:
            if lista[i]>lista[i+1]:
                c=c+1
            elif i==(len(lista)-1):
                if lista[i]>lista[i-1]:
                    c=c+1
                else:
                    if lista[i]>lista[i+1] and lista[i]>lista[i-1]:
                        c=c+1
    if c==1:
        return True
    else:
        return False
a=[]
b=[]
n=int(input('Digite a quantidade de elementos das lista':))
for i in range(1,n+1,1):
    valor=float(input('Digite o valor :'))
    a.append(valor)
for i in range(1,n+1,1):
    valor=float(input('Digite o valor :'))
    b.append(valor)
if lecker(a):
    print('N')
else:
    print('S')
if lecker(b):
    print('N')
else:
    print('S')    