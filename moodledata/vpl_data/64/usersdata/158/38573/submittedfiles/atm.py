# -*- coding: utf-8 -*-
from __future__ import division
import math
saque=int(input('digite valor do saque:'))
a=saque//20
b=saque%20
c=(saque%20)//10
d=(saque%20)%10
e=(saque%20)%10//5
f=(saque%20)%10%5
g=(saque%20)%10%5//2
h=(saque%20)%10%5%2
i=(saque%20)%10%5%2//1
if b==0 or b!=0:
    print(a)
if d==0 or d!=0:
    print(c)
if f==0 or f!=0:
    print(e)
if h==0 or h!=0:
    print(g)
if i==0 or i!=0:
    print(j)