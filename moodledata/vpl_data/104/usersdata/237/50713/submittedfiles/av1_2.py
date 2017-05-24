# -*- coding: utf-8 -*-
import math
N=int(input("Digite o N: "))
a=N/2
x1=int(input("Digite x1: "))
y1=int(input("Digite y1: "))
x2=int(input("Digite x2: "))
y2=int(input("Digite y2: "))
if (N//2)==0:
    if x1<=a and y1<=a and x2<=a and y2<=a:
        print("N")
    elif x1<=a and y1>a and x2<=a and y2>a:
        print("N")
    elif x1>a and y1<=a and x2>a and y2<=a:
        print("N")
    elif x1>a and y1>a and x2>a and y2>a:
        print("N")
    else:
        print("S")
else:
    print("N não é par...")