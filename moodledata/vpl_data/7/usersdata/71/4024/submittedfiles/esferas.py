# -*- coding: utf-8 -*-
from __future__ import division

a = input("Insira o peso a: ")
b = input("Insira o peso b: ")
c = input("Insira o peso c: ")
d = input("Insira o peso d: ")

if a==b+c+d and b+c==d and b==c:
    print("S")
else:
    print("N")