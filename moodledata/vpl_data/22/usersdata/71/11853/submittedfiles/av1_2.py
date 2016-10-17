# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input("Insira a Sequência: ")

a=n//1000
b=(n//100)%10
c=(n//10)%10
d=n%10

if a==c or b==d:
    print("V")
else:
    print("F")
    