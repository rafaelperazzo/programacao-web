# -*- coding: utf-8 -*-
from __future__ import division

#escreva suas funcoes aqui
f = 0.2
dH = input('Digite a perda de carga: ')
L = input('Digite o comprimento da tubulação: ')
Q = input('Digite a vazão: ')
g = input('Digite a gravidade: ')

#DELTA H PARA ENCONTRAR D
def D(H,f,L,Q,g):
    q = Q**2
    a = (3,1415)**2
    
    A = (8*f*L*q)
    B = H*a*g
    
    d = (A/B)**(1/5)
    
    return d
    
print D
    
#REY

def Rey(Q,D,v):
    a = (3,1415)
    A = 4*Q
    B = a*D*v
    
    R = (A/B)
    
    return R
    
def F(Rey,e,D):
    A = ((64/Rey)**8) + 9.5
    B = (e/(3.7*D)) + (5.74/(Rey**0.9))
    C = (2500/Rey)**6
    
    f = (A * ((math.log(B) - C)**(-16)))**0.125
    return f
    