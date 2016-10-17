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
BVP-BVP-BVP
Nota-se que que os valores repetidos representam a parte
branca correspondente a cor da cobra
logo, sempre que uma das variações dessa forma aparecerem a coral será verdadeira""" 

if b!=a and b==d and b!=c or a==c and a!=b and a!=d:
    print 'V'
else:
    print 'F'