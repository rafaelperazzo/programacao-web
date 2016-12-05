# -*- coding: utf-8 -*-
from __future__ import division

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

    