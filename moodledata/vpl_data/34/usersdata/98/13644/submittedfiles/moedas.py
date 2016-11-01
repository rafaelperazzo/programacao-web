# -*- coding: utf-8 -*-
from __future__ import division

a=input('Digite o valor de a: ')
b=input('Digite o valor de b: ')
c=input('Digite o valor de c: ')

na=c//a
r=c%a
nb=r//b

if r%b==0:
    print(na)
    print(nb)
else:
    nb=c//b
    r=c%b
    na=r//a
    if r%a==0:
        print(na)
        print(nb)
    else:
        print('N')