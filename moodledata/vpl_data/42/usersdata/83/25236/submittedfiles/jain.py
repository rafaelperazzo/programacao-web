# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

f = 0.2
dH = input('Digite a perda de carga: ')
L = input('Digite o comprimento da tubulação: ')
Q = input('Digite a vazão: ')
g = input('Digite a gravidade: ')
v = input('Digite a viscosidade cinemática: ')
e = input('Digite a rugosidade absoluta: ')
k = 10

import math

def diametro_do_tubo(f,L,Q,g,dH):
    diametro=((8*f*L*(Q**2))/((math.pi**2)*g*dH))**(1/5)
    return diametro

def reynalds(Q,D,v):
    rey=(4*Q)/(math.pi*D*v)
    return rey

def fator(r,e,D):
    c=(64/r)**8
    b=((e/(3.7*D))+(5.74/(r**0.9)))
    y=(2500/r)**6
    a=(c+(9.5*(((math.log(b)-y)**(-16)))))**0.125
    return a


while(True):
    D= diametro_do_tubo(f,L,Q,g,dH)
    r= reynalds(Q,D,v)
    fn= fator(r,e,D)
    if 0.000001<=(e/D)<=0.01 and 5000<=r<=100000000:
        if abs(f-fn<0.000001):
            break
        else :
            f=fn
    
print ('O diametro do tubo é %.5f' %D)
print ('A força de atrito será %.5f' %fn)