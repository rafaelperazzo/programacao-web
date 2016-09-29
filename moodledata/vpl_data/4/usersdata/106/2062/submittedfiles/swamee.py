# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI
#entrada
f = input ('Digite um valor para f')
L = input ('Digite um valor para L')
Q = input ('Digite um valor para Q')
deltaH = input ('Digite um valor para deltaH')
v = input ('Digite um valor para v')

#processamento:
g= 9.81
E = 0.000002
pi = math.pi

D= (( 8*f*L*(Q**2))/((pi**2)*g*deltaH))**0.2
print ('%.4f' %D)