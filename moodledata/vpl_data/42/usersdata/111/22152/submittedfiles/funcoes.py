# -*- coding: utf-8 -*-
from __future__ import division
import math

#escreva suas funcoes aqui

def D(f,L,Q,g,dH):
    
    Di=((8*f*L*(Q**2))/((pi**2)*g*dH))**0.2
    return Di
    
Di=D(f,L,Q,g,dH)
  
def Rey(Q,Di,v):
    
    R=((4*Q)/(pi*Di*v))
    return R
    
R=Rey(Q,Di,v)
    
def F(R,E):
    
    fn=((64/R)**8 + 9.5*((log(((E)/(3.7*Di)) + ((5.74)/(R**0.9))) - ((2500/R)**6))**-16))**0.125
    return fn
    
    
    
    











































