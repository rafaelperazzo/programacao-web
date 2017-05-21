# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('digite o valor de a:'))
b=int(input('digite o valor de b:'))
c=int(input('digite o valor de c:'))
soma=0
somab=0
i=a
j=b
while i<=c:
    soma=soma+1
    i=i+a
print(soma)

resto=c%a
while j<=resto:
    somab=somab+1
    j=j+b
print(somab)



