# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
a=int(input('Digite um número'))
b=int(input('Digite um número'))
c=int(input('Digite um número'))
troco=0
qa=c//a
while qa>=0:
    troco=c%a
    if troco%a==0:
        print(qa)
    if troco%b==0:
        qb=troco//b
        break
    if troco%b==1:
        qa=qa-1
        
