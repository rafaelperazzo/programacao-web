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

for i in range(1,k+1,1):
#   Calculando D:
    D= funcoes.diametro(f,L,Q,g,dH)

#   Calculando Rey:
    rey= funcoes.calculorey(Q,D,v)
    
#   Calculando fprox:
    fprox= funcoes.fn1(rey,e,D)
    if math.fabs(f-fprox)<0.000001:
        break
    else:
        f=fprox
print('%.10f'%D)
print('%.10f'%fprox)