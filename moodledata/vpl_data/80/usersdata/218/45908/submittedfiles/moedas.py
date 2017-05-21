# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('digite o valor de a:'))
b=int(input('digite o valor de b:'))
c=int(input('digite o valor a ser trocado:'))
na=0
nb=0
resto=0
if a>b:
    na=c//a
    resto=c%a
    nb=resto//b
    valora=na*a
    valorb=nb*b
    if (valora+valorb)==c:
        print(na)
        print(nb)
    else:
        print('N')
else:
    nb=c//b
    resto=c%b
    na=resto//a
    valora=na*a
    valorb=nb*b
    if (valora+valorb)==c:
        print(na)
        print(nb)
    else:
        print('N')    