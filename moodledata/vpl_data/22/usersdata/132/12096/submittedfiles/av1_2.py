# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('digite um numero entre zero e nove:')
b=input('digite um numero entre zero e nove:')
c=input('digite um numero entre zero e nove:')
d=input('digite um numero entre zero e nove:')
if a==c and a!=b and b!=d:
    print('V')
if b==d and b!=c and b!=a and a!=c:
    print('V')
    