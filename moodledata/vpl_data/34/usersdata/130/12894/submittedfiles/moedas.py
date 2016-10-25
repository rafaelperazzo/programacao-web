# -*- coding: utf-8 -*-
from __future__ import division
a=input('Digite o valor de a:')
b=input('Digite o valor de b:')
c=input('Digite o valor de c:')
if a>=b:
    qa=0
    qb=0
    if c%a==0:
        qa=c//a
        print(qa)
        print(qb)
    else:
        qa=c//a
        d=c%a
        if d%b==0:
            qb=d//b
            print(qa)
            print(qb)
        else:
            print('N')
else:
    qb=0
    qa=0
    if c%b==0:
        qb=c//b
        print(qb)
        print(qa)
    else:
        qb=c//b
        d=c%b
        if d%a==0:
            qa=d//a
            print(qb)
            print(qa)
        else:
            print('N')
            
            