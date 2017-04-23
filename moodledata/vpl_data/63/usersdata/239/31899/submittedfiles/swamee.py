# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f = float(input("Digite aqui o valor de f: "))
l = float(input("Digite aqui o valor de l: "))
q = float(input("Digite aqui o valor de q: "))
DH = float(input("Digite aqui o valor de Delta H: "))
v = float(input("Digite aqui o valor de v: "))
g = 9.81
e = 0.000002
math.pi
D = ((8*f*l*q*q)/(math.pi**2*g*DH))**1/5
print("D=%.4f"%D)
Rey = (4*q)/(math.pi*D*v)
print("Rey=%.4f"%Rey)
k = 0.25/(math.log10((e)/(3.7*D))+(5.74)/((Rey**0.9))**2)
print("k=%.4f"%k)
