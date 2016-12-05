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

def diametro(f,L,Q,dH):     #Diametro do tubo#
    Diametro=(8*L*Q*Q*f)/(dH*math.pi*math.pi*g)**(1/5)
    return Diametro
    
def Reynolds(v,Q,D):        #número de Reynolds#
    Rey=4*Q/(v*D*math.pi)
    return Rey
    
def Atrito(D,E,Rey):        #fator de atrito#
    f=(((64/Rey)**8)+9.5*((math.log(5.74/(Rey**0.9))+(E/(D*3.7)))-(2500/Rey)**6))**(-16)))**0.125
    return f
    
for i in range(0,k,1):
    d=diametro(f,dH,L,Q)
    Reynol=Reynolds(Q,v,d)
    at=Atrito(e,Reynol,d)
    if 0.000001<=(e/d)<=0.01 and 5000<=Reynol<=100000000:
        if at==f:
            break
        else:
            f=at
print('%.10f'%d)
print('%.10f'%f)
