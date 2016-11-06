# -*- coding: utf-8 -*-
from __future__ import division

n=input('Insira a quantidade de números: ')

l=[]

somaimpar=0
somapar=0
qimpar=0
qpar=0

for i in range (0,n,1):
    l.append(input('Digite um número: '))
    
    if l[i]%2!=0:
        somaimpar=somaimpar+l[i]
        qimpar=qimpar+1
    else:
        somapar=somapar+l[i]
        qpar=qpar+1
    
print somaimpar
print somapar
print qimpar
print qpar
print l