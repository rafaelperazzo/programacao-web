# -*- coding: utf-8 -*-
from __future__ import division
import math

# Equação para calcular o diãmetro da tubulação:
def diametro(f,L,Q,g,dH):
    D= ((8*f*L*(Q**2))/((math.pi**2)*g*dH))**0.2
    return D
    
#Equação para calcular o Rey:
def calculorey(Q,D,v):
    rey= (4*Q)/(math.pi*D*v)
    return rey
    
# Equação do fn+1:
def fn1(rey,e,D,):
    fprox= (((64/rey)**8)+(9.5*((math.log((e/(3.7*D))+(5.74/(rey**0.9)))-((2500/rey)**6))**-16)))**0.125
    return fprox