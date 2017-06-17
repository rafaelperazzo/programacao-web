# -*- coding: utf-8 -*-
from __future__ import division

def pmax(a):
    for i in range (0, len(n)-1,1):
        if n[i]>n[i+1]:
            cont=cont+1
            return True
        else:
        return False
a=[]
n =int(input('Digite a quantidade de elementos da lista: '))
for i in range (0,n+1,1):
    valor=int(input('Valor: '))
    a.append(valor)
if pico(a):
    print('S')
else:
    print('N')
    

