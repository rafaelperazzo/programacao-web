# -*- coding: utf-8 -*-
from __future__ import division
import math
a = input('Digite um numero:')
b = input('Digite um numero:')
c = input('Digite um numero:')
d = input('Digite um numero:')
"""sabemos que se a coral for verdadeira teremos:
    BVBP-BVBP 
Já se a cobra for falsa, teremos: 
BVP-BVP-BVP""" 
if b!=a and b==d and b!=d:
    print 'V'
else:
    print 'F'