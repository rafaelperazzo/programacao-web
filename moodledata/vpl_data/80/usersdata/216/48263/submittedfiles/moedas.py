# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('Digite um número:'))
b=int(input('Digite um número:'))
c=int(input('Digite um número:'))

qa=c//a
cont=1
qb=0

while qa>=0:
    troco=c-(qa*a)
    if troco%b==1:
        qb=troco//b
        cont=cont+1
        break
    else:
        qa=qa-1
if cont>0:
    print(qa)
    print(qb)
else:
    print('Não')