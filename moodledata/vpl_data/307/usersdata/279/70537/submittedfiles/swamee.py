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
D=float=((8*F*L*(Q**2)/((math.pi**2)*g*H))**(1/5))
print("%.4f"%D)
REY=float=(4*Q/(math.pi*D*v))
print("%.4f"%REY)
k=float=(0.25/((math.log10(e/(3.7*D)+(5.74/(REY**0.9))))**2))
print("%.4f"%k)






