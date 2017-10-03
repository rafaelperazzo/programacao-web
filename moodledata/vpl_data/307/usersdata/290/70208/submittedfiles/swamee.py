# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f=float(input("Digite o valor de f: "))
L=float(input("Digite o valor de L: "))
Q=float(input("Digite o valor de Q: "))
VH=float(input("Digite o valor de VH: "))
v=float(input("Digite o valor de v: "))
g=(9.81)
E=(0.000002)
D=(((8*f*L*Q*Q)/(math.pi*math.pi*g*VH))**(0.2))
Rey=((4*Q)/(math.pi*D*v))
k=(0.25/((math.log10((E/(3.7*D))+(5.74/Rey**(0.9))))**2))