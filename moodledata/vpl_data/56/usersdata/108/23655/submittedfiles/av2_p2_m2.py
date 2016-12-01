# -*- coding: utf-8 -*-
from __future__ import division

n = input ('Digite o número de salas:')
e = input ('Digite a porta de entrada:')
s = input ('Digite a porta de saída:')

l = []
for i in range (0,n,1):
    l.append ('Digite a quantidade de vidas:')
    
soma=0

if (e==s):
    soma = l[e]

elif (e<s):
    for i in range (e,s+1,1):
        soma = soma + l[i]

else:
    for i in range (s,e+1,1):
        soma = soma + l[i]
        
print (soma)
        
