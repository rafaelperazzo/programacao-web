# -*- coding: utf-8 -*-
from __future__ import division
a=input('digite o valor da moeda a:')
b=input('digite o valor da moeda b:')
c=input('digite o valor da nota:')
if c%a==0 and c%b!=0:
    print(c//a)
    print(0)
if c%a!=0 and c%b==0:
    print(0)
    print(c//b)
if c%a==0 and c%b==0 and a>=b:
    x=a
    y=b
    qa=c//x
    qb=(c%x)//y
    qc=(c%x)%y
    if qc!=0:
        print('N')
    else:
        print(qa)
        print(qb)
if c%a==0 and c%b==0 and a<b:
    x=b
    y=a
    qb=c//x
    qa=(c%x)//y
    qc=(c%x)%y
    if qc!=0:
        print('N')
    else:
        print(qa)
        print(qb)
if c%a!=0 and c%b!=0 and a>=b:
    x=a
    y=b
    qa=c//x
    qb=(c%x)//y
    qc=(c%x)%y
    if qc!=0:
        print('N')
    else:
        print(qa)
        print(qb)
if c%a!=0 and c%b!=0 and a<b:
    x=b
    y=a
    qb=c//x
    qa=(c%x)//y
    qc=(c%x)%y
    if qc!=0:
        print('N')
    else:
        print(qa)
        print(qb)        
    