# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input("Insira a: ")
b = input("Insira b: ")
mdc=1
if a=>b:
    c=b
else:
    c=a
for i in range (1,c+1,1):
    if a%i==0 and b%i==0:
        mdc=i
    i=i+1
print mdc