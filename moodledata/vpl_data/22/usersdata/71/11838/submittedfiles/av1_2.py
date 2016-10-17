# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input("Insira a Sequência: ")

d=n%10
c=(n//10)%10
b=(n//100)%10
a=(n//1000)

print a
print b
print c
print d

if a==c or b==d:
    print("V")
else:
    print("F")
    