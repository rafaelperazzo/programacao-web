# -*- coding: utf-8 -*-
from __future__ import division
import math

#escreva suas funcoes aqui

def D(f,L,Q,g,dH):
    
    Di=((8*f*L*(Q**2))/((pi**2)*g*dH))**0.2
    return Di
    
def Rey(Q,D,v):
    
    Rey=((4*Q)/(pi*D*v))
    return Rey
    
def f2(Rey,E,D):
    
    fn=((64/Rey)**8 + 9.5*((log(((E)/(3.7*D)) + ((5.74)/(Rey**0.9))) - ((2500/Rey)**6))**-16))**0.125
    return fn
    
    
    
    











































