# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('digite o valor de a:'))
b=int(input('digite o valor de b:'))
c=int(input('digite o valor a ser trocado:'))
cont=0
valor=0
i=0
if a>=b:
    n=a
    m=b
else:
    n=b
    m=a
while cont==0:
    valor=(c-(n*i))
    if valor%m==0:
        cont=1
i=i+1
print(i-1)
print(c//m)