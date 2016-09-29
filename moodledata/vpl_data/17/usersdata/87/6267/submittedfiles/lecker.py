# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input("Digite valor de a:")
b = input("Digite valor de b:")
c = input("Digite valor de c:")
d = input("Digite valor de d:")

if a>b:
    contador=contador + 1
if a<b>c:
    contador=contador + 1
if b<c>d:
    contador=contador + 1
if d>c:
    contador=contador + 1
if contador==1:
    print("S")
else:
    print("N")