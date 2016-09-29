# -*- coding: utf-8 -*-
from __future__ import division
import math


a=input('Digite o valor de a: ')
b=input('Digite o valor de b: ')
c=input('Digite o valor de c: ')
d=input('Digite o valor de d: ')

i=0

if a>b:
    i=i+1
if b>a and b>c:
    i=i+1
if c>a and c>d:
    i=i+1
if d>c:
    i=i+1
if i==1:
    print 'S'
else:
    print 'N'





