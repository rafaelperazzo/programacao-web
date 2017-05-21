# -*- coding: utf-8 -*-
n=int(input('digite n:'))
a=float(input('digite a:'))
b=float(input('digite b:'))
h=(b-a)/n
soma=0
i=i+h
while i<b-h:
    soma=soma+(i**2)-4
    i=i+h
soma=soma*2
resultado=((a**2)-4+(b**2)-4)+soma*(h/2)
print(resultado)