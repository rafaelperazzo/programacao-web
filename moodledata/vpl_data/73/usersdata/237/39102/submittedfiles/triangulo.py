# -*- coding: utf-8 -*-
import math
a=float(input("Digite a: "))
b=float(input("Digite b: "))
c=float(input("Digite c: "))
if  a<b+c :
    if (a*a)==(b*b)+(c*c):
        print("Re")
    elif (a*a)>(b*b)+(c*c):
        print("Ob")
    elif (a*a)<(b*b)+(c*c):
        print("Ac")
    if a==b==c:
        print("Eq")
    elif b==c!=a or b!=c==a or b==a!=c:
        print("Is")
    elif a!=b!=c:
        print("Es")
else:
    print("N")