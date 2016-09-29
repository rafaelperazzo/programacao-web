# -*- coding: utf-8 -*-
from __future__ import division

p1 = input("Digite valor de p1:")
c1 = input("Digite valor de c1:")
p2 = input("Digite valor de p2:")
c2 = input("Digite valor de c2:")

if p1*c1==p2*c2:
    print("0")
if p1*c1>p2*c2:
    print("-1")
if p1*c1<p2*c2:
    print("1")