# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
a=float(input('digite a:'))
b=float(input('digite b:'))
n=float(input('digite n:'))
h=(b-a)/n
s=0
i=a+h
while i<=b-h:
    s=s+((i**3)-(4*i)-5)
    i=i+h
fa=(a**3)-(4*a)-5
fb=(b**3)-(4*b)-5
I=(h/2)*(fa+fb+2*s)
print(I)