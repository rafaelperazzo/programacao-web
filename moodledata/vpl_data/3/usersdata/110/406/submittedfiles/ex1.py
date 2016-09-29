# -*- coding: utf-8 -*-
from __future__ import division
a=input('Digite a:')
b=input('Digite b:')
c=input('Digite c:')
delta=b**2 - 4*a*c
if delta<0 :
    print('Não existe raíz real')
else:
    r1= (-b+(delta)**0.5)/2*a
    r2=(-b -(delta)**0.5)/2*a
    print(r1)
    print(r2)
