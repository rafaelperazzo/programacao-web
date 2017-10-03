# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
#ENTRADA
f = float(input("Valor de f: "))
L = float(input("Valor de L: "))
Q = float(input("Valor de Q: "))
DeltaH = float(input("Valor de delta H: "))
V = float(input("valor de V: "))
#PROCESSAMENTO
D = ((8*f*L*(Q**2))/((3.14159**2)*9.81*DeltaH))**(1/5)
Rey = (4*Q)/(3.14159*D*V)
K = (0.25)/math.log10(((0.000002*3.7*D)+5.74)/(Rey**0.9))**2
#SAIDA
print("%.4f" %D)
print("%.4f" %Rey)
print("%.4f" %K)