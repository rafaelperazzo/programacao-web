# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO ABAIXO DESTA LINHA

a = int(input("digite valor da primeira carta: "))
b = int(input("digite valor da segunda carta: "))
c = int(input("digite valor da terceira carta: "))
d = int(input("digite valor da quarta carta: "))
e = int(input("digite valor da quinta carta: "))

if a<b<c<d<e:
    print("C")
if a>b>c>d>e:
    print("D")
else:
    print("N")

