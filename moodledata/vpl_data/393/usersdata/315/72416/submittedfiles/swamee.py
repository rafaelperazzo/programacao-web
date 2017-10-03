# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI

# CONSTANTES
g = 9.81
e = 0.000002

#ENTRADAS
f = float(input('Digite valor de f: '))
L = float(input('Digite valor de L: '))
Q = float(input('Digite valor de Q: '))
DH = float(input('Digite valor de DH: '))
v = float(input('Digite valor de v: '))

#FORMULA PARA D
x = (8*f*L*(Q**2))
y = ((math.pi**2)*g*DH)
D = (x/y)**(1/5)

#FORMULA PARA REY
Rey = (4*Q)/(math.pi*D*v)

#FORMULA PARA K
z = e/3.7*D
p = 5.74/(Rey**0.9)
k = 0.25/(math.log10(z+p))**2

#SAIDAS
print ('%.4f' %D)
print ('%.4f' %Rey)
print ('%.4f' %k)

