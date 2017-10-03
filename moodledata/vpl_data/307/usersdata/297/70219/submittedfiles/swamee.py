# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f = float(input('digite um valor qualquer; '))
L = float(input('digite um valor qualquer: '))
Q = float(input('digite um valor qualquer; '))
deltaH = float(input('digite um valor qualquer; '))
v = float(input('digite um valor qualquer; '))
g = 9.81
epsilon = 0.000002
D = (((8*f*L*Q**2)/math.pi**2*g*deltaH)**(1/5))
print(input('%.4f ' %D))
Rey = ((4*Q)/math.pi*D*v)
print(input('%.4f ' %Rey))
k = ((0.25)/(math.log10(((epsilon)/3.7)+((5.74)/Rey**0.9)))**2
print(input('%.4f ' %k ))