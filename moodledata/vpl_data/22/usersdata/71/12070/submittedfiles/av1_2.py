# -*- coding: utf-8 -*-
from __future__ import division
import math

a=input("a: ")
b=input("b: ")
c=input("c: ")
d=input("d: ")

if a==c or b==d:
    if a==b or c==d:
        print("F")
    elif a==c and b==d:
        print("F")
    else:
        print("V")
else:
    print("F")
    