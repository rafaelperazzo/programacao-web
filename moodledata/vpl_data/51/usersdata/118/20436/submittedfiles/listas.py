# -*- coding: utf-8 -*-
from __future__ import division

def degrau(lista):
    maior = 0
    for i in range(0,len(lista)-1,1):
        s = (lista[i]) - (lista[i+1])
        if s > 0 and s > maior:
            maior = s
        elif s < 0:
            s = (-1)*s
            if s > maior:
                maior = s
            
    return maior
    
n = int(input('Digite o número de termos maior que dois:'))
a = []
for i in range(0,n,1):
    a.append(input('Digite um valor:'))

print('%.d' % degrau(a))
