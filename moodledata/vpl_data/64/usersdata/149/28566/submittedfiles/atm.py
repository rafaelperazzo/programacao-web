# -*- coding: utf-8 -*-
from __future__ import division
import math
r1=0
r2=0
r3=0
r4=0
r5=0
V=int(input('digite o valor que quer sacar:'))
v1=V//20
r1=V%v1
v2=r1//10
if v2>0:
    r2=r1%v2
v3=r2//5
if v3>0:
    r3=r2%v3
v4=r3//2
if v4>0:
    r4=r3%v4
v5=r4//1
if v5>0:
    r5=r4%v1
print v1
print v2
print v3
print v4
print v5