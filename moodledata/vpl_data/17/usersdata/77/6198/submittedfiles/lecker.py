# -*- coding: utf-8 -*-
from __future__ import division
import math

a=input('Digite um valor a:')
b=input('Digite um valor b:')
c=input('Digite um valor c:')
d=input('Digite um valor d:')
contador=0

if a>b:
    contador=contador+1
if b>a and b>c: 
    contador=contador+1
if c>b and c>d:
    contador=contador+1
if d>c:
    contador=contador+1

if contador==1:
    print('S')
else:
    print('N')
