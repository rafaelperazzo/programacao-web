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

fn = 0.2
dH = input('Digite a perda de carga: ')
L = input('Digite o comprimento da tubulação: ')
Q = input('Digite a vazão: ')
g = input('Digite a gravidade: ')
v = input('Digite a viscosidade cinemática: ')
e = input('Digite a rugosidade absoluta: ')
k = 10
#comece aqui

import math

def diametro(fn,L,Q,dH):
    Diam=((8*fn*L*Q*Q)/(math.pi*math.pi*dH*g))**(1/5)
    return Diam

def Reynalds(Q,D,v):
    R=4*Q/(math.pi*D*v)
    return R

def atrito(Rey,E,D):
    s=(E/(3.7*D))+(5.74/(Rey**0.9))
    t=(2500/Rey)**6
    f=(((64/Rey)**8)+9.5*((math.log(s)-t)**(-16)))**0.125
    return f
    

for i in range(0,k,1):
    D=diametro(fn,L,Q,dH)
    Rey=Reynalds(Q,D,v)
    fn=atrito(Rey,e,D)
    if 0.000001<=(e/D)<=0.01 and 5000<=Rey<=100000000:
        if fn==f:
            break
        else:
            f=fn
print('%.10f'%f)
print('%.10f'%D)