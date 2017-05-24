# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
a=int(input('Digite um número:'))
b=int(input('Digite um número:'))
c=int(input('Digite um número:'))
qa=c//a
while qa>0:
    qa=c//a
    troco=c%a
    if troco%a==0:
        qa=troco//a
    if troco%b==0:
        qb=troco//b
        break
    if troco%b==1:
        qa=qa-1
print(qa)
print(qb)
