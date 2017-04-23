# -*- coding: utf-8 -*-
p1=float(input("digite o primeiro peso: "))
c1=float(input("digite o primeiro comprimento: "))
p2=float(input("digite o segundo peso: "))
c2=float(input("digite o segundo comprimento: "))
a=p1*c1
b=p2*c2
if a==b:
    print("0")
if a>b:
    print("-1")
if a<b:
    print("1")

