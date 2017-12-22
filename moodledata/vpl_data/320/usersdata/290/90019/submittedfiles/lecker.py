# -*- coding: utf-8 -*-
import math
a=float(input("Digite o valor de a: "))
b=float(input("Digite o valor de b: "))
c=float(input("Digite o valor de c: "))
d=float(input("Digite o valor de d: "))
while a>b:
    if b>c or c>b or c>d or d>c:
        print("N")
    else:
        print("S")
