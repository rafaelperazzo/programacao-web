# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('digite a: '))
b=int(input('digite b: '))
c=int(input('digite c: '))
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
    print('N')

    