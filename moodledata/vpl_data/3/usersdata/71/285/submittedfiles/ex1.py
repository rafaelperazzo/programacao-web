# -*- coding: utf-8 -*-
from __future__ import division

a = input("Insira o Valor de a: ")
b = input("Insira o Valor de b: ")
c = input("Insira o Valor de c: ")

delta = b**2-(4*a*c)

if delta<0:
    print("A Equação Não Possui Raízes Reais.")
    
else:
    x1 = (-b+(delta**0.5))/2*a
    x2 = (-b-(delta**0.5))/2*a
    print("%.2f" x1)
    print("%.2f" x2)
    
