# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input("Insira o valor de a: ")
b = input("Insira o valor de b: ")
c = input("Insira o valor de c: ")
d = input("Insira o valor de d: ")

if a>b and b>=c and c>=d:
    print("S")
elif a<b and b>c and c>=d:
    print("S")
elif a<=b and b<c and c>d:
    print("S")
elif a<=b and b<=c and c<d:
    print("S")
else:
    print("N")