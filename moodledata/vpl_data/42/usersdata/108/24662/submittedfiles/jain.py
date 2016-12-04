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

#início do programa:

i = 1
D = 0
Rey = 0
fn = 0 #fator inicial
ff = 0 #fator final

# as variavéis 'a' e 'b' serão usadas para realizar o cálculo do ff (fator de atrito posterior) em partes.
a = 0
b = 0

# i fará o papel de contador. 
while (i<=k):
    if (f!=fn):
        D = ((8*f*L*(Q**2))/((math.pi**2)*g*dH))**(1/5)
        Rey = ((4*Q)/(math.pi*D*v))
        a = ((2500/Rey)**6)
        b = (1/(((math.log10 ((e/(3.7*D))+(5.74/(Rey**0.9))))-a)**16))
        ff = ((((64/Rey)**8) + 9.5*b)**0.125)
        
    # ao final, o fator inicial receberá o valor de f=0.2 e o valor do fator final receberá será armazenado na variável f.
        fn=f
        f=ff
        
    i=i+1
   
print ('%.10f' %D)
print ('%.10f' %ff)