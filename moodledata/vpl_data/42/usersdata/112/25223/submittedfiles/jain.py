# -*- coding: utf-8 -*-
from __future__ import division
import funcoes
import math

f = 0.2
dH = input('Digite a perda de carga: ')
L = input('Digite o comprimento da tubulação: ')
Q = input('Digite a vazão: ')
g = input('Digite a gravidade: ')
v = input('Digite a viscosidade cinemática: ')
e = input('Digite a rugosidade absoluta: ')
k = 10



Dfinal = funcoes.defineD(f, g, v, Q, dH, L, e, k)
ffinal = funcoes.definef(f, g, v, Q, dH, L, e, k)

print 'D=%.4f' %Dfinal
print 'f=%.4f' %ffinal