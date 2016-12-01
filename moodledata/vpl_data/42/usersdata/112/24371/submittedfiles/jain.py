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
pi=3.1415
''' 
AINDA NÃO TERMINEI O TRABALHO, POR FAVOR, NÃO CORRIJA AINDA
#comece aqui
def ln(n):
    if n == 0 or n < 0:
       return "Math Domain Error"
    if n == 1:
       return 0
    if n > 0 and n < 1:
       return loge(n,0,-n-80)
    else:
       return loge(n,0,n)

D=((8*f*L*(Q**2))/(dH*(pi**2)*g))**(1/5)
Rey=(4*Q)/(pi*D*v)
fn=(((64/Rey)**8)+95*(ln((e/3.1*D)+(5.47/(Rey**0.9)))-(2500/Rey)**6)**-16)**0.125
