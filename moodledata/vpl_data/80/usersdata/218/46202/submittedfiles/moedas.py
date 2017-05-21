# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('digite o valor de a:'))
b=int(input('digite o valor de b:'))
c=int(input('digite o valor a ser trocado:'))
valor=0
i=0
if a>=b:
    n=a
    m=b
else:
    n=b
    m=a
while i<=m:
    valor=(c-(n*i))
    if valor%m==0:
        break
i=i+1
if cont==0:
    print('N')
print(i-1)
print(c//m)