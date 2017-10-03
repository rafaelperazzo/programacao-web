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

D=((8*f*l*(q**2))/(math.pi*g*dh))**1/5
Rey=(4*q)/(math.pi*D*v)
k=0.25/(math.log10((e/(3.7*D))+(5.74/(Rey**0.9)))**2)




