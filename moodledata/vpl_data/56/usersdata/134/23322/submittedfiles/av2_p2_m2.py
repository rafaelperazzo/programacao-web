# -*- coding: utf-8 -*-
from __future__ import division

def vidas(a,e,s):
    pont = 0
    if a[e]<a[s]:
        for i in range(e,s+1,1):
            pont = pont + a[i]
    if a[s]<a[e]:
        for i in range(s,e+1,1):
            pont = pont + a[i]
    
    return pont
    
n = input('Quantidade de salas:')
pe = input('Porta de entrada:')
ps = input('Porta de saída:')
v = []

for i in range(0,n,1):
    v.append(input('Digite um valor:'))
    
print vidas(v,pe,ps)
    

            
    

