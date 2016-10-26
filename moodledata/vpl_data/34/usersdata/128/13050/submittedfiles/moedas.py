# -*- coding: utf-8 -*-
from __future__ import division

a=input('Digite o valor de uma moeda: ')
b=input('Digite o valor de outra moeda: ')
c=input('Digite o valor da cédula: ')

qa=0
qb=0
contA=0

while qa<=c:
    qa=qa+a
    contA=contA+1

while qb<(c-(contA*a)):
    qb=qb+b
    contB=contB++1

print contA
print contB