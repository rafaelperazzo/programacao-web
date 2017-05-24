# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
a=int(input('Digite um número:'))
b=int(input('Digite um número:'))
c=int(input('Digite um número:'))
qa=c//a
qb=0
while qa>=0:
    troco=c-(qa*a)
    if troco%a==0:
        qa=troco//a
    if troco%b==0:
        qb=troco//b
    if troco%b==1:
        qa=qa-1
print(qa)
print(qb)
