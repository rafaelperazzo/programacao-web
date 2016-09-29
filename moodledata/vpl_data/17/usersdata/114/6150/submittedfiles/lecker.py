# -*- coding: utf-8 -*-
from __future__ import division
import math

a=input('valor para a: ')
b=input('valor para b: ')
c=input('valor para c: ')
d=input('valor para d: ')

if a>b<=c<=d or a<b>c<=d or a<=b<c>d or a<=b<=c<d:
    print('S')
else:
    print('N')