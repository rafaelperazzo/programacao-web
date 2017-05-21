# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('digite o valor de a:'))
b=int(input('digite o valor de b:'))
c=int(input('digite o valor da celula:'))
i=c//a

for i in range(1,c+1,1):
    resto=c-(a*i)
    if resto>=b:
        qb= resto//b
        if (resto%b)==0:
            print(i)
            print(qb)
        else:
            print('N')
    i=i-1    




