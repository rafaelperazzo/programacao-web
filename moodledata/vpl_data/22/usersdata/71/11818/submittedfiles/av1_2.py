# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input("a: ")
b=input("b: ")
c=input("c: ")
d=input("d: ")

n=input("Insira a Sequência: ")

d=n%10
c=d%10
b=c%10
a=b%10

print a
print b
print c
print d

if a==c or b==d:
    print("V")
else:
    print("F")
    