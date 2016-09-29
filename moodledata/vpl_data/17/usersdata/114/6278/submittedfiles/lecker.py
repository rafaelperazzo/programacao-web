# -*- coding: utf-8 -*-
from __future__ import division
import math

a=input('valor para a: ')
b=input('valor para b: ')
c=input('valor para c: ')
d=input('valor para d: ')

if a>b:
    contador=contador+1
if a<b>c:
    contador=contador+1
if b<c>d:
    contador=contador+1
if c<d:
    contador=contador+1
    print('S')
else:
    print('N')
    