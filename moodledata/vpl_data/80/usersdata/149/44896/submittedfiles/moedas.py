# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('digite o valor de a:'))
b=int(input('digite o valor de b:'))
c=int(input('digite o valor de c:'))
if a%c=0 and b%c=0:
    print('N')
else: 
soma=0
i=a
while i<=c:
    if a%c=0 or b%c=0:
    soma=soma+1
    i=i+a
print(soma)

j=b
somab=0
resto=c%a
while j<=resto:
    if b%c=0 or a%c=0:
    somab=somab+1
    j=j+b
print(somab)