# -*- coding: utf-8 -*-
from __future__ import division
import math

#escreva suas funcoes aqui

def definicao_do_D(f, g, v, Q, dH, L,):
        for i in range(0 , k , 1):
            D = ((8*f*L*(Q**2))/(dH*(math.pi**2)*g))**(0.2)
            Rey = (4*Q)/(math.pi*D*v)
            fn = (((64/Rey)**8)+9.5*(math.log((e/3.7*D)+(5.47/(Rey**0.9)))-(2500/Rey)**6)**-16)**0.125
            f = fn
        return f,D

