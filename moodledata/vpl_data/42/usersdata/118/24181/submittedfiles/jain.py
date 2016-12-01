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


D = funcoes.Diametro(f,L,Q,g,dH)
Rey = funcoes.Rey(f,L,Q,g,dH,v)
fn = funcoes.fn(f,L,Q,g,dH,v,e)

if f == fn:
    print('%.10f' % D)
    print('%.10f' % fn)
else:
    f = fn
    for i in range(0,k,1):
        D = funcoes.Diametro(f,L,Q,g,dH)
        Rey = funcoes.Rey(f,L,Q,g,dH,v)
        fn = funcoes.fn(f,L,Q,g,dH,v,e)
        if f == fn:
            print('%.10f' % D)
            print('%.10f' % fn)
            break
        else:
            f = fn