# -*- coding: utf-8 -*-
from __future__ import division
import math

n = input("Insira o N. de termos: ")

soma=0

for i in range (1,n+1,1):
    a=(i/(i**2))
    if i%2==0:
        a=a*(-1)
    soma=soma+a
print ("%.5f" %soma)