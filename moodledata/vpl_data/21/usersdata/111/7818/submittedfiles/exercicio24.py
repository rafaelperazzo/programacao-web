# -*- coding: utf-8 -*-
from __future__ import division
import math

a=int(input("Digite a:" ))
b=int(input("Digite b:" ))

i=1
while i<=a and i<=b:
    if a%i==0 and b%i==0: 
        print i
        break
    i=i+1