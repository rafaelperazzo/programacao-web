# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
a = float(input("Investimento inicial: "))
b = float(input("Percentual: "))
A1 = a+a*b
A2 = A1+(A1*b)
A3 = A2+(A2*b)
A4 = A3+(A2*b)
A5 = A4+(A4*b)
A6 = A5+(A5*b)
A7 = A6+(A6*b)
A8 = A7+(A7*b)
A9 = A8+(A8*b)
A10 =A9+(A9*b)
#SAIDA
print("%.2f" %A1)
print("%.2f" %A2)
print("%.2f" %A3)
print("%.2f" %A4)
print("%.2f" %A5)
print("%.2f" %A6)
print("%.2f" %A7)
print("%.2f" %A8)
print("%.2f" %A9)
print("%.2f" %A10)