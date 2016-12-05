# -*- coding: utf-8 -*-
from __future__ import division

#escreva suas funcoes aqui

def fD(f,L,Q,g,dH):
    D=((8*f*L*(Q**2))/(((math.pi)**2)*g*dH))**0.2
    return D
    
def fRey(v,f,L,Q,g,dH):
    D= fD(f,L,Q,g,dH)
    Rey=(4*Q)/(math.pi*D*v)
    return Rey
    
def FuncaoAtrito(f,L,g,dH,Q,v):
    D= fD(f,L,Q,g,dH)
    Rey= fRey(v,f,L,Q,g,dH)
    
    fn1=(math.log((e/(3.7*D))+(5.74/(Rey**0.9))))-((2500/Rey)**6)
    fn2= 9.5*((fn1)**(-16))
    fn3= ((fn2)+((64/Rey)**8))**(0.125)
    return fn3
