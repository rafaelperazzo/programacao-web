# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('digite um valor:')
b=input('digite um valor:')
c=input('digite um valor:')
d=input('digite um valor:')
contador=0
if a<b:
    contador=contador+1
if a>b>c:
    contador=contador+1
if b<c<d:
    contador=contador+1
if c<d:
    contador=contador+1
if contador==1:
    print "s"
else:
    print "s"