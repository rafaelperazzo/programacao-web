# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
F=float=input('digite o valor de F')
L=float=input('digite o valor de L')

Q=float=input('digite o valor de Q')
H=float=input('digite o valor de H')
v=float=input('digite o valor de v')
g=float=9.81
e=float=0.000002
D=((8*F*L*(Q**2)/(math.pi**2*g*H))**(1/5))
print(D)
REY=(4*Q/(math.pi*D*v))
print(REY)








