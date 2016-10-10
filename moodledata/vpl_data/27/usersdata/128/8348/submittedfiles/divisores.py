# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('Digite a quantidade de múltiplos: ')
a=input('Digite o primeiro número: ')
b=input('Digite o sesundo número: ')

for i in range (0, n, 1):
    if i%a==0 or i%b==0:
        print i