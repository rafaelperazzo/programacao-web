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


D = ((8*f*L*(Q**2))/(dH*(math.pi**2)*g))**(1/5)
Rey = (4*Q)/((math.pi)*D*v)
fn = (((64/Rey)**8)+95*(math.log((e/3.1*D)+(5.47/(Rey**0.9)))-(2500/Rey)**6)**-16)**0.125


if fn==f:
   
    print D
    print f

Dfinal= funcoes.defineD(f, g, v, Q, dH, L, e, k)
ffinal= funcoes.definef(f, g, v, Q, dH, L, e, k)

print Dfinal
print ffinal