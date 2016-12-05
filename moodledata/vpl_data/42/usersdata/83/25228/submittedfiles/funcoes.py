# -*- coding: utf-8 -*-
from __future__ import division

#escreva suas funcoes aqui

def diametro_do_tubo(f,L,Q,g,deltah):
    diametro=[(8*f*L*(Q**2))/((math.pi**2)*g*deltah)]**(1/5)
    return diametro

def reynalds(Q,D,v):
    rey=(4*Q)/(math.pi*D*v)
    return rey

def fator_de_atrito(r,e,D):
    parte1=((64/r)**8)
    parte2=math.log[((e)/(3,7*D))+((5,74)/(r**0.9))]
    parte3=((2500/r)**6)
    
    atrito={parte1+9.5*[(parte2-parte3)**(-16)]}**0.125
    
    return atrito
    