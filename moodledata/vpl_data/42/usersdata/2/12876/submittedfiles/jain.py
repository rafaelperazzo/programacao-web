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
def main(f,dH,L,Q,g,v,e,k):
    print('f\t D\t e/d\t\t Rey\t\t fProx') 
    for i in range(0,k,1):
        D = darcy(dH,f,L,Q,g)
        Rey = reynolds(Q,D,v)
        fProx = jain(e,D,Rey)
        ed = e/float(D)
        print('%.6f\t %.6f\t %.10f\t %.6f\t %.6f\n' % (f,D,ed,Rey,fProx))        
        f = fProx
    return (D,f)

print(main(f,dH,L,Q,g,v,e,k))
