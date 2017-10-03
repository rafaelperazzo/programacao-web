# -*- coding: utf-8 -*-
from math import sqrt
print("-----------------------------------------------------------")
print("Bem vindo ao meu mundo de cálculos!!! Divirta-se
print("-----------------------------------------------------------")
a=float(input("Digite a: "))
b=float(input("Digite b: "))
c=float(input("Digite c: "))
Delta=(b**2)-4*a*c
if Delta>=0:
    x1=(-b+sqrt(Delta))/(2*a)
    x2=(-b-sqrt(Delta))/(2*a)
    print("%.2f"%x1)
    print("%.2f"%x2)
else:
    print("SRR")
    
