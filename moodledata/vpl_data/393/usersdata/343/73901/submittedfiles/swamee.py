# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI

#ENTRADA
g = 9.81
E = 0.000002

f = float(input('Digite um valor para f: '))
L = float(input('Digite um valor para L: '))
Q = float(input('Digite um valor para Q: '))
dH = float(input('Digite um valor para dH: '))
s = float(input('Digite um valor para s: '))
p = float(input('Digite um valor para p: '))

#PROCESSAMENTO
D = ((8*f*L*(Q**2))/((math.pi**2)*g*dH))**0.2