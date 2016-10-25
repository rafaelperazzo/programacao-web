# -*- coding: utf-8 -*-
from __future__ import division
import math
#escreva suas funcoes aqui
def raizN(n,x):
    return x**(1/float(n))

def darcy(dH,f,L,Q,g):
    D = raizN(5,(8*f*L*Q*Q)/(math.pi*math.pi*g*dH))
    return D

def reynolds(Q,D,v):
    rey = ((4*Q)/(math.pi*D*v))
    return rey
    
def jain(e,D,Rey):
    den = (e/(3.7*D)) + (5.74/(Rey**(0.9)))
    f = 0.25/(math.log10(den)*math.log10(den))
    return f

def jainGeral(e,D,Rey):
    a = (64/Rey)**8
    b = math.log((e/(3.7*D))+(5.74/(Rey**(0.9))))
    c = (2500/Rey)**6
    parte1 = 9.5*((b-c)**(-16))
    parte2 = (a + parte1)**(0.125)
    
    return parte2