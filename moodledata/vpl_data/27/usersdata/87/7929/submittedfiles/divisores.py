# -*- coding: utf-8 -*-
from __future__ import division
import math

n = input("valor de n:")
a = input("valor de a:")
b = input("valor de b:")

i=1
j=1
while i<=n:
    if j%a==0 or j%b==0:
        print(j)
        i=i+1
    j=j+1
