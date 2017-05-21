# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('digite o valor de A:'))
b=int(input('digite o valor de B:'))
c=int(input('digite o valor de C:'))
if a>b:
    ma=a
    me=b
else:
    ma=b
    me=a
if c%ma==0:
    qma=c//ma
else:
    while c>me:
        if c%me==0:
            qme=c//me
            break
        else:
            c=c-ma
            ma=ma+1
    
