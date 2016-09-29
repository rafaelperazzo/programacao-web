# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input("Insira o valor de a: ")
b = input("Insira o valor de b: ")
c = input("Insira o valor de c: ")
d = input("Insira o valor de d: ")

i = 0

if a>b:
    i=i+1
if b>a and b>c:
    i=i+1
if c>b and c>d:
    i=i+1
if d>c:
    i=i+1
if i==1:
    print("S")
else:
    print("N")
