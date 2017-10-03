# -*- coding: utf-8 -*-
import math
f=float(input("Digite o valor de f: "))
L=float(input("Digite o valor de L: "))
Q=float(input("Digite o valor de Q: "))
g=float(9.81)
e=float(0.000002)
v=float(input("Digite o valor de v: "))
DeltaH=float(input("Digite o valor de DeltaH: "))
#Valor de D
numeradorD=float(8*f*L*(Q**2))
denominadorD=float((math.pi**2)*g*DeltaH)
D=float(((numeradorD/denominadorD)**0.2))
print("%.4f"%D)
#Valor de Rey
numeradorRey=float(4*Q)
denominadorRey=float(math.pi*D*v)
Rey=float(numeradorRey/denominadorRey)
print("%.4f"%Rey)
#Valor de k
x=float(e/(3.7*D))
y=float(5.74/(Rey**0.9))
k=(0.25/(math.log10(x*y)**2))
print("%.4f"%k)
