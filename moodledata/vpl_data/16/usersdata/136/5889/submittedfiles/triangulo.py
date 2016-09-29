# -*- coding: utf-8 -*-
from __future__ import division
import math
a = input("Digite o valor do lado a:")
b = input("Digite o valor do lado b:")
c = input("Digite o valor do lado c:")

if a < b + c:
    print("S")
    if a**2 == b**2 + c**2:
        print("Re")
    if a**2 > b**2 + c**2:
        print("Ob")
    if a**2 < b**2 + c**2:
        print("Ac")
    if a == b == c:
        print("Eq")
    if b == c != a:
        print("Is")
    if a != b != c:
        print("Es")
else:
    print("N")