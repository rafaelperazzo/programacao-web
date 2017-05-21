# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('digite o valor da primeira moeda:'))
b=int(input('digite o valor da segunda moeda:'))
c=int(input('digite o valor da cédula:'))
qma=0
qme=0
if a>=b:
    ma=a
    me=b
else:
    ma=b
    me=a
if (c%ma)==0:
    qma=(c/ma)
    qme=0
else:
    while c>=me:
        if (c%me)==0:
            qme=(c/me)
            break
        else:
            c=c-ma
            qma=qma+1
if c<me:
    print('N')
else:
    if a>=b:
        print('%d'qma)
        print('%d'qme)
    else:
        print('%d'qme)
        print('%d'qma)