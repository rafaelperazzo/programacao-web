# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI

f = input("Insira f: ")
L = input("Insira L: ")
Q = input("Insira Q: ")
dH = input("Insira dH: ")
v = input("Insira v: ")

pi = math.pi
g = 9.81
e = 000002

D = ((8*f*L*Q*Q)/(pi*pi*g*dH))*(1/5)

Rey = (4*Q)/(pi*D*v)

k = 0,25/(math.log10((e/(3.7*D))+(5.74/(Rey**0.9))))**2

print("D= %.4f" %D)
print("Rey= %.4f" %Rey)
print('k= %.4f' %k)