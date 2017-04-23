# -*- coding: utf-8 -*-
import math
a=int(input('Digite lado 1: '))
b=int(input('Digite lado 2: '))
c=int(input('Digite lado 3: '))
a=a>=b
b=b>=c
c=c>0
if (a**2)==(b**2+c**2):
    print('Retângulo')
if (a**2)>(b**2+c**2):
    print('Obtusângulo')
if (a**2)<(b**2+c**2):
    print('Acutângulo')
if a==b and b==c:
    print('Retângulo')
if b==c and c!=a:
    print('Isósceles')
if a!=b and b!=c:
    print('Escaleno')
