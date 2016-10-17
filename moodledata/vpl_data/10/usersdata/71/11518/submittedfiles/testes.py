# -*- coding: utf-8 -*-
from __future__ import division

a = input("Insira um Número: ")
b = input("Insira Outro Número: ")
c = a*b
mdc = 1
i=2

while i<=c:
    if a%i==0 and b%i==0:
        mdc=i
    i=i+1
print mdc
    