# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('digite a:')
b=input('digite b:')
c=input('digite c:')
d=input('digite d:')
if b==d and a!=c and a!=b and a!=d and b!=c and c!=d:
    print ('V')
elif a==c and b!=d and a!=b and a!=d and b!=c and c!=d:
    print ('V')
elif a!=b and a!=c and a!=d and b!=c and b==d and c!=d:
    print ('V')
elif a!=b and a==c and a!=d and b!=c and b!=d and c!=d:
    print ('V')
else:
    print ('F')


