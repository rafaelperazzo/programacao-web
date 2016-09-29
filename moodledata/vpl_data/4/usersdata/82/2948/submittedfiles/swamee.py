# -*- coding: utf-8 -*-
from __future__ import division
import math

f = input ('digite f:')
L = input ('digite L:')
Q = input ('digite Q:')
DeltaH = input ('digite DeltaH:')
v = input ('digite v:')

D = ((8*f*L*(Q)**2)/((math.pi)**2*g*DeltH))**1/5
Rey = (4*Q)/(math.pi*D*v)
K = (0.25)/((math.log10)*((E/(3.7*D))+((5.74)/((Rey)**0.9)))

Print (' o valor de D eh %.4f' %D)
Print (' o valor de Rey eh %.4f' %Rey)
Print ('o valor de K eh %.4f')



