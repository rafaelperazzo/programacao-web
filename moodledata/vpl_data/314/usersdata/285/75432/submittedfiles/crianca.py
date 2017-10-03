# -*- coding: utf-8 -*-
p1=float(input("digite o valor de p1: "))
c1=float(input("digite o valor de c1: "))
p2=float(input("digite o valor de p2: "))
c2=float(input("digite o valor de c2: "))
if (p1*c1)==(p2*c2):
    print("0")
elif(p1*c1)>(p2*c2):
    print("-1")
else:
    print("1")