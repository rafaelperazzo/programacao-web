# -*- coding: utf-8 -*-
from __future__ import division

n=input('Insira a quantidade de números: ')

somaimpar=0
somapar=0
qimpar=0
qpar=0

for i in range (0,n,1):
    x=input('Digite um número: ')
    
    if x%2!=0:
        somaimpar=somaimpar+x
        qimpar=qimpar+1
    else:
        somapar=somapar+x
        qpar=qpar+1
    
print somaimpar
print somapar
print qimpar
print qpar