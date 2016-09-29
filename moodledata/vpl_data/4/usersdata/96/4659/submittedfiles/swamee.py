# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI
F=input('Digite o valor de f: ')
L=input('Digite o valor de l: ')
Q=input('Digite o valor de q: ')
DH=input('Digite o valor de dh: ')
V=input('Digite o valor de v: ')
G=9.81
E=0.000002
D=((8*F*L*(Q**2))/((math.pi**2)*G*DH))**(1/5)
Rey=((4*Q)/(math.pi*D*V))
A=((E/3.7*D)+(5.74/Rey**(9/10)))
K=((0.25)/((log10(A))**2)
print D
print Rey
print K