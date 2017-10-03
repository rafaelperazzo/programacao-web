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
D=((8*f*L*Q*Q)**0.2)/((math.pi*math.pi*g*deltaH)**0.2)
print('%.4f' %(D))
Rey= (4*Q)/(math.pi*D*v)
print('%.4f' %(Rey))
K= (0.25/(math.log10((E/(3.7*D))+(5.74/(Rey**0.9))))**2)
print('%.4f' %(K))


