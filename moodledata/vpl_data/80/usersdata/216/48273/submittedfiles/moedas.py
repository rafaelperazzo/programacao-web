# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('Digite um valor de moeda:'))
b=int(input('Digite um valor de moeda:'))
c=int(input('Digite um valor de cédula:'))

qa=c//a
cont=0
qb=0

while qa>=0:
    troco=c-(qa*a)
    if troco%b==0:
        qb=troco//b
        cont=cont+1
        break
    else:
        qa=qa-1
if cont>0:
    print(qa)
    print(qb)
else:
    print('N')