# -*- coding: utf-8 -*-
from __future__ import division
import funcoes
import math

'''
ENTRADA TESTE
f = 0.2
dH = 5
L = 3250
Q = 0.005
g = 9.81
v = 0.000001
e = 0.00006
k = 10
A saida para esta entrada é aproximadamente: 0.1247 (D) e 0.0224 (f)
'''

f = 0.2
dH = input('Digite a perda de carga: ')
L = input('Digite o comprimento da tubulação: ')
Q = input('Digite a vazão: ')
g = input('Digite a gravidade: ')
v = input('Digite a viscosidade cinemática: ')
e = input('Digite a rugosidade absoluta: ')
k = 10
pi=3.1415

#comece aqui


D=((8*f*L*(Q**2))/(dH*(pi**2)*g))**(1/5)
Rey=(4*Q)/(pi*D*v)
fn=(((64/Rey)**8)+95*(math.log((e/3.1*D)+(5.47/(Rey**0.9)))-(2500/Rey)**6)**-16)**0.125
if fn==f:
    print D
    print f

if fn!=f:
    def novo_D_novo_f(fn):
        NovoD=((8*fn*L*(Q**2))/(dH*(pi**2)*g))**(1/5)
        return NovoD
print novoD        