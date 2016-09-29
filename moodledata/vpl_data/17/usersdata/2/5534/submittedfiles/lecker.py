# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
d = input('Digite d: ')

cont = 0

if a>b:
    cont = cont + 1
if b>a and b>c:
    cont = cont + 1
if c>b and c>d:
    cont = cont + 1
if d>c:
    cont = cont + 1

if cont==1:
    print('S')
else:
    print('N')
