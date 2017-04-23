# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f = float(input("Digite aqui o valor de f: "))
l = float(input("Digite aqui o valor de l: "))
q = float(input("Digite aqui o valor de q: "))
deltah = float(input("Digite aqui o valor de Delta H: "))
v = float(input("Digite aqui o valor de v: "))
g = 9.81
e = 0.000002
pi=math.pi
D=((8*f*l*(q**2))/((math.pi**2)*g*deltah))**(1/5)
print("%.4f"%D)
Rey = (4*q)/(math.pi*D*v)
print("%.4f"%Rey)
k = 0.25/(math.log10((e)/(3.7*D))+(5.74)/((Rey**0.9))**2)
print("%.4f"%k)
