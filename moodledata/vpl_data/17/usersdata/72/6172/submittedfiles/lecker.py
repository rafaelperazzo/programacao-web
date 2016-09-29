# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
a=input('digite o valor da variável a:')
b=input('digite o valor da variável b:')
c=input('digite o valor da variável c:')
d=input('digite o valor da variável d:')

#SAIDA
if a>b:
    contador=contador+1
if b>c and b>a:
    contador=contador+1
if c>d and c>b:
    contador=contador+1
if d>c:
    contador=contador+1
if contador==1:
    print 'S'
else:
    print 'N'
