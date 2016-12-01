# -*- coding: utf-8 -*-
from __future__ import division
n=input('salas:')
a=[]
for i in range (0,n,1):
    a.append('vidas:')
    
entrada=input('entrada')
saida=input('saida')

def vidas(a,entrada,saida):
    soma=0
    for i in range (entrada,saida+1,1):
        soma=soma+a[i]
    return soma
print vidas(a,entrada,saida)