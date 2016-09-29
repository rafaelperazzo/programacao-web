# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI
#ENTRADA
f = input("Digite o valor de f:")
L = input("Digite o valor de L:")
Q = input("Digite o valor de Q:")
H = input("Digite o valor de deltaH:")
v = input("Digite o valor de v:")
#PROCESSAMENTO
D = ((8*f*L*(Q**2))/((math.pi**2)*9.81*H))**0.5
rey = (4*Q)/(math.pi*D*v)
k = 0.25/(math.log10((0.000002/3.7*D)+(5.74/Rey**0.9)))**2
#SAIDA
print("O valor de D é %.4f" %D)
print("O valor de Rey é %.4f" %Rey)
print("O valor de k é %.4f" %k)