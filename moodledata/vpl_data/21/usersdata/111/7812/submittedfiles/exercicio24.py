# -*- coding: utf-8 -*-
from __future__ import division
import math

a=int(input("Digite a:" ))
b=int(input("Digite b:" ))

i=2
while true:
    if a%i == b%i: 
        print i
        break
    i=i+1