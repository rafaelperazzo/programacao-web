# -*- coding: utf-8 -*-
from __future__ import division
import math
a =  input ('digite o valor 1:')
b =  input ('digite o valor 2:')
n =  input ('digite o intevalo:')
for i in range (1, (n/2)+1,1):
    c=i*a
    d=i*b
    if  c == d:
        print c
    elif c>d:
        print d
        print c
    else:
        print c
        print d
