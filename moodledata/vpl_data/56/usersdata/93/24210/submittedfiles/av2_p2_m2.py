# -*- coding: utf-8 -*-
from __future__ import division
n=input('n: ')
a=[]
for i in range(0,n,1):
    a.append(input('numero de vida da sala: '))
b=input('porta de entrada: ')
c=input('porta de saida: ')
soma=0
for i in range(0,len(a),1):
    if i>=b and i<=c:
        soma=soma+a[i]
print soma
        

