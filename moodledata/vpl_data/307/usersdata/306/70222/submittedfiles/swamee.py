# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
print("----------------------------------\nFormula para encontar o valor de K\n----------------------------------")

f=float(input("--------------\nDigite f: "))
l=float(input("\nDigite l: "))
q=float(input("\nDigite q: "))
dh=float(input("\nDigite variação de h: "))
v=float(input("\nDigite v: "))
print("--------------")
g=9.81
e=0.000002
pi=3.14
D=((8*f*l*(q*q))/(pi*g*dh))**0.2
Rey=(4*q)/(pi*D*v)
k=0.25/(math.log10((e/(3.7*D))+(5.74/(Rey**0.9)))**2)

print("%.4f"%D)
print("%.4f"%Rey)
print("%.4f"%k)

print("--------------\nFIM DO PROGRAMA")




