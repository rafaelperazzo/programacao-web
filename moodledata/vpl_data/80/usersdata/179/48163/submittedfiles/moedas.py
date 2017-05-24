# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('digite o valor de a :'))
b=int(input('digite o valor de b:'))
c=int(input('digite o valor de c :'))
cont=0
qa=c//a
qb=0
while qa>=0:
    tr=c-qa*a
    if tr%b==0:
        qb=tr//b
        cont=cont+1
        break
    else:
        qa=qa-1
if cont>0:
    print(qa)
    print(qb)
else:
    print('n')
        

  