# -*- coding: utf-8 -*-
from __future__ import division
import math
print('Programa que verifica três lados formam um triângulo e o classifica')
a=input('Digite o valor de a:')
b=input('Digite o valor de b:')
c=input('Digite o valor de c:')
if a<b+c and b<a+c and c<b+a:
    print('S')
    if (a*a)==(b*b)+(c*c) or (b*b)==(a*a)+(c*c) or (c*c)==(a*a)+(b*b):
        print('Re')
        if (a==b)and (a==c):
            print('Eq')
        elif (a=b and a!=c) or (b=c and b!=a) or (c=a and c!=b):
            print('Is')
        elif a!=b and a!=c and b!=c:
        print('Es')
    elif (a*a)>(b*b)+(c*c) or (b*b)>(a*a)+(c*c) or (c*c)>(a*a)+(b*b):
        print('Ob')
    elif (a*a)<(b*b)+(c*c) or (b*b)<(a*a)+(c*c) or (c*c)<(a*a)+(b*b):
        print('Ac')
    
else:
    print('N')
