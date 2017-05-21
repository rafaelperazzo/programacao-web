# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('Digite o valor de a: '))
b=int(input('Digite o valor de b: '))
c=int(input('Digite o valor de c: '))
if c%a!=0 and c%b!=0:
    a=a*0
    b=b*0
    print('N')
soma=0
i=a
while i<=c:
    soma=soma+1
    i=i+a
print(soma)
j=b
somab=0
resto=c%a
while j<=resto:
    somab=somab+1
    j=j+b
print(somab)    