# -*- coding: utf-8 -*-
import math
a=int(input("Digite a: "))
b=int(input("Digite b: "))
c=int(input("Digite c: "))
d=int(input("Digite d: "))

if a>b:
    if c>b and c>d or d>c:
        print("N")
    else:
        print("S")
elif b>a and b>c:
    if c>b and c>d or d>c:
        print("N")
    else:
        print("S")
elif c>b and c>d:
    if a>b:
        print("N")
    else:
        print("S")
elif d>c:
    if b>a and b>c:
        print("N")
    else:
        print("S")
else:
    print("N")