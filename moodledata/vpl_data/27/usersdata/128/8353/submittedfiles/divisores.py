# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('Digite a quantidade de múltiplos: ')
a=input('Digite o primeiro número: ')
b=input('Digite o sesundo número: ')

m=0
c=1

for c in range (1,n+1,1):
    if m%a==0 or m%b==0:
        print m
    m=m+1
    