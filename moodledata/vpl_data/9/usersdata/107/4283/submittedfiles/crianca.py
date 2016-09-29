# -*- coding: utf-8 -*-
from __future__ import division
p1=input('digite o valor de p1:')
c1=input('digite o valor de c1:')
p2=input('digite o valor de p2:')
c2=input('digite o valor de c2:')
if ((c1*p1)==(c2*p2)):
    print(0)
if ((c1*p1)<(c2*p2)):
    print(-1)
if ((c1*p1)>(c2*p2)):
    print(1)