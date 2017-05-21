# -*- coding: utf-8 -*-
import math
b=float(input('Digite o valor de b: '))
a=float(input('Digite o valor de a: '))
n=float(input('Digite o valor de n: '))
n=int(n)
h=(b-a)/n
S=0
i=a+h
while i<=(b-h):
    fi=(i**3)-(4*i)-(5)
    S=S+fi
    i=i+h
fa=(a**3)-(4*a)-(5)
fb=(b**3)-(4*b)-(5)
I=(h/2)*(fa+fb+(2*S))
print(I)

