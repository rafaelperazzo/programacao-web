# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input("digite a:")
b=input("digite b:")
c=input("digite c:")
d=input("digite d")

if  a < b < c < d or a > b > c > d or a < b > c > d or a < b < c > d: 
    print("S")
    
else:
    print("N")