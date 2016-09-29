# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input("Digite valor de a:")
b = input("Digite valor de b:")
c = input("Digite valor de c:")
d = input("Digite valor de d:")

if a>b and a!=c and a>c and a!=d:
    print("S")
if b>a and b>c and b!=d:
    print("S")
if c!=a and c>a and c>b and c>d:
    print("S")
if d!=a and d>a and d!=b and d>b and d>c:
    print("S")
else:
    print("N")