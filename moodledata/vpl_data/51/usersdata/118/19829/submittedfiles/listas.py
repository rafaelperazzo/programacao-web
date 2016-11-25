# -*- coding: utf-8 -*-
from __future__ import division

def degrau(lista):
    
    for i in range(0,len(lista),1):
        maior = 0
        s = lista[i] - lista[i+1]
        if s >= 0 and s > maior:
            return s
        elif s < 0 and ((-1)*s) > maior:
            return ((-1)*s)
            
n = int(input('Digite o número de termos maior que dois:'))
a = []
for i in range(0,n,1):
    a.append(input('Digite um valor:'))

print('%.d' % degrau(a))
