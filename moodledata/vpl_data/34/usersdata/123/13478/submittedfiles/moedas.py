# -*- coding: utf-8 -*-
from __future__ import division
a= input('Insira a:')
b= input('Insira b:')
c= input('Insira c:')

qa= c//a
qb= (c%a)//b

if ((qa*a)+(qb*b))==c:
    print (qa)
    print (qb)
else:
    print('N')