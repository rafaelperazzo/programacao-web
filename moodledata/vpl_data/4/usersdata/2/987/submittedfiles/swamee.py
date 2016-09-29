# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI
f = input('Digite f: ')
L = input('Digite L: ')
Q = input('Digite Q: ')
deltaH = input('Digite Delta H: ')
v = input('Digite v:')

g = 9.8
e = 0.000002

D = ((8*f*L*Q*Q)/(math.pi*math.pi*g*deltaH))**(0.2)
