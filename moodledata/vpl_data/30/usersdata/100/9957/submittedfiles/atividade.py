# -*- coding: utf-8 -*-
from __future__ import division
import math

n = input("Insira n: ")
if n<0:
    n=n*(-1)
soma = 0
for i in range (1,n+1,1):
    a = i/(n+1-i)
    soma = soma+a
print ('%.5f'%soma)