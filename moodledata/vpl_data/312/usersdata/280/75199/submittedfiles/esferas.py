# -*- coding: utf-8 -*-
a=float(input("Insira a: "))
b=float(input("Insira b: "))
c=float(input("Insira c: "))
d=float(input("Insira d: "))
if a==b+c+d and b+c==d and b==c:
    print("S")
else:
    print("N")