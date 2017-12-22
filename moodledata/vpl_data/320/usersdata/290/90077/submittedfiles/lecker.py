# -*- coding: utf-8 -*-
import math
a=float(input("Digite o valor de a: "))
b=float(input("Digite o valor de b: "))
c=float(input("Digite o valor de c: "))
d=float(input("Digite o valor de d: "))
while (True):
    if (a<b and b<c and c<d) or (a<b and c<b and d<c) or (b>a and c>b and c>d) or (a>b and b>c and c>d) or (a>b and b==c and c==d) or (a==b and b==c and c<d) or (a<b and b==c and c<d) or(a>b and b==c and c>d) or (a==b and b<c and c>d) or (a>b and a==c and a==d):
        print("S")
    else:
        print("N")
    
