# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input("digite n:")
a=0
i=1
if n<0:
    n=n*(-1)

while i<=n:
    a=a+i/(n-(i-1))
    i=i+1
print("%.5f" %a)

    