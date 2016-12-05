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

import math

def diametrotubo(f,L,Q,dH,g):     #Diametro do tubo#
    Diametro=((8*L*f*(Q**2))/((math.pi**2)*dH*g))**(1/5)
    return Diametro
    
def numeroReynolds(v,Q,D):        #número de Reynolds#
    Rey=(4*Q)/(v*D*math.pi)
    return Rey
    
def FatorAtrito(D,e,Rey):        #fator de atrito#
    x=((e/(3.7*D))+(5.74/(Rey**0.9)))
    y=(2500/Rey)**6
    z=(64/Rey)**8
    f=(z+(9.5*(((math.log(x)-y)**(-16)))))**0.125
    return f
    
for i in range(0,k,1):
    d=diametrotubo(f,L,Q,dH,g)
    Reynol=numeroReynolds(v,Q,d)
    at=FatorAtrito(D,e,Reynol)
    if 0.000001<=(e/D)<=0.01 and 5000<=Reynol<=100000000:
        if at==f:
            break
        else:
            f=at
print('Diâmetro do tubo:%.10f'%D)
print('Força do atrito:%.10f'%at)
