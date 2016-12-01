# -*- coding: utf-8 -*-
from __future__ import division
import math

#Funções
def Diametro(f,L,Q,g,dH):
    D = (((8*f*L*(Q**2))/((math.pi**2)*g*dH))**0.2)
    return D

def Rey(f,L,Q,g,dH,v):
    D = Diametro(f,L,Q,g,dH)
    
    R = (4*Q)/(math.pi*D*v)
    return R

def fn(f,L,Q,g,dH,v,e):
    D = Diametro(f,L,Q,g,dH)
    R = Rey(f,L,Q,g,dH,v)
    
    s3 = (((64/R)**8)+ 9.5*((math.log((e/(3.7*D))+(5.74/(R**0.9)))-((2500/R)**6))**-16))**0.125
    return s3