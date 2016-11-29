# -*- coding: utf-8 -*-
from __future__ import division
import funcoes


'''
ENTRADA TESTE
f = 0.2
dH = 5
L = 3250
Q = 0.005
g = 9.81
v = 0.000001
E = 0.00006
k = 10
A saida para esta entrada é aproximadamente: 0.1247 (D) e 0.0224 (f)
'''

Di=funcoes.D(f,L,Q,g,dH)

R=funcoes.Rey(Q,Di,v)


k=10
for i in range(0,k,1):
    
    Di=funcoes.D(f,L,Q,g,dH)
    R=funcoes.Rey(Q,Di,v)
    f = 0.2
    dH = input('Digite a perda de carga: ')
    L = input('Digite o comprimento da tubulação: ')
    Q = input('Digite a vazão: ')
    g = input('Digite a gravidade: ')
    v = input('Digite a viscosidade cinemática: ')
    E = input('Digite a rugosidade absoluta: ')
    
    Diametro=funcoes.D(f,L,Q,g,dH)

    print ('%.10f ' %Diametro)

    fn=funcoes.F(R,E,Di)

    print ('%.10f ' %fn)
    
    if f==fn:
        break
  

    
































































