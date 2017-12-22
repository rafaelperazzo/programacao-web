# -*- coding: utf-8 -*-
import math

a=int(input("Digite a: "))
b=int(input("Digite b: "))
c=int(input("Digite c: "))
d=int(input("Digite d: "))
cont=0
for i in range (1,5,1):
    if i==1 and a>b:
        cont= cont+1
    elif i==2 and b>a and b>c:
        cont= cont+1
    elif i==3 and c>b and c>d:
        cont= cont+1
    elif i==4 and d>c:
        cont= cont+1
if cont==1:
    print("S")
else:
    print("N")