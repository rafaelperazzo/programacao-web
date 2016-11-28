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


#comece aqui
D= funcoes.calcula_D(f,L,Q,g,dH)
Rey= funcoes.calcula_Rey(Q,v,f,L,g,dH)
fProx= funcoes.calcula_fator_de_atrito(Q,v,f,L,g,dH,e)
while True:
    if abs(f-fProx<0.000001):
        f=fProx
        fProx=calcula_fator_de_atrito(Q,v,f,L,g,dH,e)
            
print f
print D
print Rey

