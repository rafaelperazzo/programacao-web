# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

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

def deltaH(f,L,Q,g,dH):
    D=((8*f*L*(Q**2))/(((math.pi)**2)g*dH))**0.2
    return D
    
def Rey(Q,D,v):
    Rey=(4*Q)/(math.pi*D*v)

def fn(Rey,e,D):
    fn= (math.log((e/(3.7*D))+5.74/((Rey**0.9)))-((2500/Rey)**(6)))**(-16)











