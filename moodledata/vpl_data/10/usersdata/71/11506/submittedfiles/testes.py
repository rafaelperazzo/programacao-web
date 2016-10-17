# -*- coding: utf-8 -*-
from __future__ import division

a = input("Insira um Número: ")
b = input("Insira Outro Número: ")
i = a*b
mdc = 0

while i>0:
    if i%a==0 and i%b==0:
        mdc=i
    i=i-1

print mdc
    