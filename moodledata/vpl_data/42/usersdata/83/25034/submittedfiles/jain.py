# -*- coding: utf-8 -*-
from __future__ import division
import funcoes
import math

'''
ENTRADA TESTE
f = 0.2
dH = 5
L = 3250
Q = 0.005
g = 9.81
v = 0.000001
e = 0.00006
k = 10
A saida para esta entrada é aproximadamente: 0.1247 (D) e 0.0224 (f)
'''

f = 0.2
dH = input('Digite a perda de carga: ')
L = input('Digite o comprimento da tubulação: ')
Q = input('Digite a vazão: ')
g = input('Digite a gravidade: ')
v = input('Digite a viscosidade cinemática: ')
e = input('Digite a rugosidade absoluta: ')
k = 10

def diametro_do_tubo(f,L,Q,g,dH):
    diametro=[(8*f*L*(Q**2))/((math.pi*math.pi*g*dH)]**(1/5)
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


while(True):
    D=diametro_do_tubo(f,L,Q,g,dH)
    r=reynalds(Q,D,v)
    fn=fator_de_atrito(r,e,D)
    if abs(f-fn<0.000001):
        break
    else :
        f=fn
    
print ('%.10f' %D)
print ('%.10f' %fn)