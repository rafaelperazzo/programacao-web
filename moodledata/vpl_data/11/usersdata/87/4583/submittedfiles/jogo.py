# -*- coding: utf-8 -*-
from __future__ import division
import math

cv = input("NUmero de vitorias do cormengo:")
ce = input("Numero de empates do cormengo:")
cg = input("NUmero de gols do cormengo:")
fv = input("NUmero de vitorias do flaminthians:")
fe = input("NUmero de empates do flaminthians:")
fg = input("NUmero de gols do flaminthians:")

c = cv*3 + ce
f = fv*3 + fe

if c>f:
    print("C")
if f>c:
    print("F")
if f==c:
    print("=")

    