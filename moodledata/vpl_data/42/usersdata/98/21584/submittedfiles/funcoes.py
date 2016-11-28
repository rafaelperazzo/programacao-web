# -*- coding: utf-8 -*-
from __future__ import division
import math
#escreva suas funcoes aqui

def calcula_D(f,L,Q,g,dH):
    D= ((8*f*L*(Q**2))/(((math.pi)**2)*g*dH))**(1/5)
    return D

def calcula_Rey(Q,v,f,L,g,dH):
    D= calcula_D(f,L,Q,g,dH)
    
    Rey= (4*Q)/((math.pi)*D*v)
    return Rey

def calcula_fator_de_atrito(Q,v,f,L,g,dH,e):
    D= calcula_D(f,L,Q,g,dH)
    Rey=calcula_Rey(Q,v,f,L,g,dH)
    
    fProx= (((64/Rey)**8)+ 9.5*(math.log((e/(3.7*D))+(5.74/(Rey**0.9))) - ((2500/Rey)**6))**(-16))**(0.125)
    
    return fProx
    
    