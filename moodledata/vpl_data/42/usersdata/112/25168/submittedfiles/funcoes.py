# -*- coding: utf-8 -*-
from __future__ import division
import math

#escreva suas funcoes aqui

def definicaodod(f, g, v, Q, dH, L, e, k):
        for i in range(0 , k , 1):
            D = ((8*f*L*(Q**2))/(dH*(math.pi**2)*g))**(0.2)
            Rey = (4*Q)/((math.pi)*D*v)
            fn = (((64/Rey)**8)+(9.5*((math.log((e/(3.7*D))+(5.74/(Rey**0.9)))-((2500/Rey)**6))**(-16)))**0.125)
            f = fn
        return D
        
def definicaodof(f, g, v, Q, dH, L, e, k):
        for i in range(0 , k , 1):
            D = ((8*f*L*(Q**2))/(dH*(math.pi**2)*g))**(0.2)
            Rey = (4*Q)/((math.pi)*D*v)
            fn = (((64/Rey)**8)+(9.5*((math.log((e/(3.7*D))+(5.74/(Rey**0.9)))-((2500/Rey)**6))**(-16)))**0.125)
            f = fn
        return f