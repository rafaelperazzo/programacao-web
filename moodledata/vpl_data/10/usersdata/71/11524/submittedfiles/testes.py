# -*- coding: utf-8 -*-
from __future__ import division

a = input("Insira um Número: ")
b = input("Insira Outro Número: ")
c=a*b
i=2

while i<=c:
    if a%i==0 and b%i==0:
        print i
        break
    i=i+1