# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('Digite a quantidade de múltiplos: ')
a=input('Digite o primeiro número: ')
b=input('Digite o sesundo número: ')

x=1

for i in range (0,n,1):
    if x%a==0 or x%b==0:
        print x
        