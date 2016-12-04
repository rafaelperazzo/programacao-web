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
D=0
Rey=0
ff=0

# as variavéis 'a' e 'b' serão usadas para realizar o cálculo do ff (fator de atrito posterior) em partes:
a=0
b=0

# i fará o papel de contador: 

while (i<=k):
    if (f!=ff):
        D = ((8*f*L*(Q**2))/((math.pi**2)*g*dH))**(1/5)
        Rey = ((4*Q)/(math.pi*D*v))
        a = ((2500/Rey)**6)
        b = (1/(((math.log10 ((e/(3.7*D))+(5.74/(Rey**0.9))))-a)**16))
        ff = ((((64/Rey)**8) + 9.5*b)**0.125)
        
    else:
        print ('%.10f' %D)
        print ('%.10f' %ff)
        break
    
    i=i+1
    f=ff
    ff=0
   
print ('%.10f' %D)
print ('%.10f' %ff)

