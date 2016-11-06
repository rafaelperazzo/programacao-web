# -*- coding: utf-8 -*-
from __future__ import division

n=input('digite o valor de n: ')
l=[]

for i in range (0,n,1):
    l.append(input('digite o valor do elemento: '))
somaimpar=0
somapar=0
for i in range (0,n,1):
    if l[i] % 2 ==1:
        somaimpar=somaimpar+l[i]
    else:
        somapar=somapar+l[i]
        
quantimpar=0
quantpar=0
for i in range (0,n,1):
    if l[i]%2!=0:
        quantimpar=quantimpar+1
     elif l[i]%2==0:
         quantpar=quantpar+1
         
print somaimpar
print somapar
print quantimpar
print quantpar
print l
        