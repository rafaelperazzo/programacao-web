# -*- coding: utf-8 -*-
from __future__ import division
a=input('digite o valor de a:')
b=input('digite o valor de b:')
c=input('digite o valor de c:')
i=c//a
while i>0:
    x=c-(i*a)
    if x>=b:
        qb=x//b
        if x%b==0:
            print(i)
            print(qb)
            else:
                print('não')