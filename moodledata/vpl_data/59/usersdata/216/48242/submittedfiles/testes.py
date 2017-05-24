# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
a=int(input('Digite um número:'))
b=int(input('Digite um número:'))
c=int(input('Digite um número:'))
qa=c//a
qb=0
cont=0
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
    print('Não')