# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
g = 9.81
E = 0.000002
f = float(input('Insira o fator de atrito f: '))
L = float(input('Insira o comprimento da tubulação em metros: '))
Q = float(input('Insira o valor da vazão em m3/s: '))
Hf = float(input('Insira a perda de carga: '))
v = float(input('Insira o valor da viscosidade do fluido: '))
#PROCESSAMENTO
D = ((8*f*L*Q**2)/((math.pi**2)*g*Hf))**(1/5)
Rey = (4*Q)/(math.pi*D*v)
k = 0.25/(math.log10((E/(3.7*D))+(5.74/Rey**0.9)))**2
print('%.4f' %k)