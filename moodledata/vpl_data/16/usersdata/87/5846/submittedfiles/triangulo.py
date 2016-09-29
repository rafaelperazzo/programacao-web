# -*- coding: utf-8 -*-
from __future__ import division
import math

a = int(input("Digite valor de a:"))
b = int(input("Digite valor de b:"))
c = int(input("Digite valor de c:"))

if a>b+c:
    print("N")
if a<b+c:
    print("S")
    if a**2==b**2+c**2:
        print("Re")
    if a**2>b**2+c**2:
        print("Ob")
    if a**2<b**2+c**2:
        print("Ac")
    if a==b==c:
        print("Eq")
    if b==c!=a:
        print("Is")
    if a!=b!=c:
        print("Es")
