# -*- coding: utf-8 -*-
from __future__ import division
a=input('digite o valor de a:')
b=input('digite o valor de b:')
c=input('digite o valor de c:')
if a>b and a>c:
    x=a
    print('o maior valor é: %.12f' %x)
elif b>a and b>c:
    y=b
    print('o maior valor é: %.12f' %y)
else:
    z=c
    print('o maior valor é: %.12f' %z)
    