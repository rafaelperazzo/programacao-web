# -*- coding: utf-8 -*-
from __future__ import division
import math 
a=input('Digite o valor de a: ')
b=input('Digite o valor de b: ')
c=input('Digite o valor de c: ')
if a>b and a>c and b>c: 
    print a
    print c
    print b
if b>a and b>c and a>c:
    print b
    print c 
    print a
if c>a and c>b and b>a:
    print c
    print a
    print b
