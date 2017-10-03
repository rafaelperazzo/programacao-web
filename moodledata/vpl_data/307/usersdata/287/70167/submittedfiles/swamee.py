# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f=float(input('Digite o valor de f'))
L=float(input('Digite o valor de L'))
Q=float(input('Digite o valor de Q'))
deltaH=float(input('Digite o valor da variação de h'))
v=float(input('Digite o valor de v'))
g=9.81
E=0.000002
D=(((8*f*L*(Q**2))**1/5)/(math.pi**2)*g*deltaH)


