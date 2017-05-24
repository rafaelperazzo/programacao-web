# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('digite o valor de A:'))
b=int(input('digite o valor de B:'))
c=int(input('digite o valor:'))
if a>b:
    ma=a
    me=b
else:
    ma=b
    me=b
if c%ma==0:
    qma=c//ma
    if a>b:
        print(qma)
        print(0)
    else:
        print(0)
        print(qma)
else:
    qme=0
    qma=0
    while c>me:
        if c%me==0:
            qme=c//me
            break
        else:
            c=c-ma
            qma=qma+1
    if qme==0:
        print('N')
    else:
        if a>b:
            print(qma)
            print(qme)
        else:
            print(qme)
            print(qma)
            
