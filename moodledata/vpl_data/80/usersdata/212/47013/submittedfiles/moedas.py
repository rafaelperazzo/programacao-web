# -*- coding: utf-8 -*-
from __future__ import division
a=float(input('digite o valor da primeira moeda:'))
a=int(a)
b=float(input('digite o valor da segunda moeda:'))
b=int(b)
c=float(input('digite o valor da cédula:'))
c=int(c)
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
    while c<=me:
        if (c%ma)==0:
            qme=(c/me)
            c=0
        else:
            c=c-ma
            qma=qma+1
if a>=b:
    print(qma)
    print(qme)
else:
    print(qme)
    print(qma)