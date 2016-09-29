# -*- coding: utf-8 -*-
from __future__ import division
import math

#ENTRADA
f =input('Digite o valor de f:')
l =input('Digite o valor de l:')
q =input('Digite o valor de q:')
deltaH =input('Digite o valor da variacao de H:')
v =input('Digite o valor de v:')
g = 9.81
e = 0.000002

#PROCESSAMENTO
superiorD =(8*f*l*(q**2))
inferiorD =(((math.pi)**2)*g*deltaH)
divD = superiorD/inferiorD
d = ((divD)**(1/5))

rey =((4*q)/((math.pi)*d*v))

funLog =((e/(3.7*d))+(5.74/((rey)**(0.9))))
funLogQuadrado =((math.log10(funLog))**2)
k =(0.25/funLogQuadrado)

#SAIDA
print('D= %.4f' %d)
print('Rey= %.4f' %rey)
print('k= %.4f' %k)
