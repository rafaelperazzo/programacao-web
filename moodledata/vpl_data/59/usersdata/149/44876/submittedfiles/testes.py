# -*- coding: utf-8 -*-
n=int(input('digite n:'))
a=float(input('digite a:'))
b=float(input('digite b:'))
h=(b-a)/n
i=a+h
soma=0
while i<=b-h:
    soma=soma+(i**2)-4
    i=i+h
soma=soma*2
resultado=(a**2)-4+(b**2)-4+soma*(h/2)
print(resultado)


print('para valores a=3 e b=13 e n=2...fica meio duvidoso...')