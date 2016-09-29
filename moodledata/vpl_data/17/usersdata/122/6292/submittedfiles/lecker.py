# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA a b c d

a=input('digite o valor de a:')
b=input('digite o valor de b:')
c=input('digite o valor de c:')
d=input('digite o valor de d:')
contador=0

#PROCESSAMENTO

if a>b:
    contador=contador+1
if b>c:
    contador=contador+1
if c>d:
    contador=contador+1
if d>c:
    contador=contador+1
if contador==1:
    print('S')
elif contador!=1:
    print('N')
