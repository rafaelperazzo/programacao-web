# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('Digite o valor da moeda a:'))
b=int(input('Digite o valor da moeda b:'))
c=int(input('Digite o valor da cédula c:'))
qa=0
qb=0
if a>=b:
    ma=a
    mb=b
else:
    ma=b
    mb=a
if c%ma==0:
    qa=c/ma
    qb=0
else:
    while c>=mb:
        if c%mb==0:
            qb=c/mb
            break
        else:
            c=c-ma
            qa=qa+1
if c<mb:
    print('N')
else:
    if a>=b:
        print('%d'%qa)
        print('%d'%qb)
    else:
        print('%d'%qb)
        print('%d'%qa)