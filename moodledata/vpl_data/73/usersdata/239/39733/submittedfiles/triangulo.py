# -*- coding: utf-8 -*-
import math
a=int(input("Digite o valor de A (escolha o lado maior): "))
b=int(input("Digite o valor de B: "))
c=int(input("Digite o valor de C: "))

if a>=b and b>=c and c>0 and a<(b+c):
    print("S")
    if (a**2)==(b**2)+(c**2):
        print("Re")
    if (a**2)>(b**2)+(c**2):
        print("Ob")
    if (a**2)<(b**2)+(c**2):
        print("Ac")
    if a==b and b==c:
        print("Eq")
    if b==c and c!=c:
        print("Is")
    if a!=b and c!=b:
        print("Es")
else:
    print("N")
