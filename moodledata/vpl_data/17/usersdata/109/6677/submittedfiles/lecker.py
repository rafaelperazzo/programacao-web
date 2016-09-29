# -*- coding: utf-8 -*-
from __future__ import division
import math

a=input('Digite o valor de a:')
b=input('Digite o valor de b:')
c=input('Digite o valor de c:')
d=input('Digite o valor de d:')

if a>b and c<b and d<b:
    print 'S'
if b>a or b>c and d<b:
    print'S'
if c>d or c>b and a<c:
    print 'S'
else:
    print 'N'