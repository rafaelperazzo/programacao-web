# -*- coding: utf-8 -*-
from __future__ import division
import math

#escreva suas funcoes aqui
def calculo(f, dH, L, Q, g, v, e, k):
    for i in range(0,k,1):
        D= ((8*f*L*(Q**2))/(((math.pi)**2)*g*dH))**(1/5)
        Rey= (4*Q)/(D*(math.pi)*v)
        f2= (((64/Rey)**8) + (9.5 * ((math.log((e/(3.7*D))+(5.74/(Rey**0.9)))-((2500/Rey)**6))**(-16)))**0.125)
        f=f2
    return (f1,D,Rey)
